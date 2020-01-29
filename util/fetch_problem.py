import base64
import os.path
import pickle
import re

from cookiecutter.main import cookiecutter
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import IPython

SCOPES = ["https://www.googleapis.com/auth/gmail.modify"]


def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            try:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "credentials.json", SCOPES
                )
            except IOError:
                print(
                    "To access to your mail's problems you must create "
                    "credentials here: "
                    "https://console.developers.google.com/apis/credentials\n"
                    "And save the client configuration file "
                    "(`credentials.json`) in this directory."
                )
                return 1
            creds = flow.run_local_server(port=0)

        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    service = build("gmail", "v1", credentials=creds)
    users = service.users()
    messages = users.messages()
    search = messages.list(
        userId="me",
        q=r"from:(founders@dailycodingproblem.com) is:inbox subject:\"Problem: Problem\"",
    )
    result = search.execute().get("messages")
    if not result:
        print("No pending problems.")
        return 0

    next_message_id = result[-1]["id"]
    next_message = messages.get(userId="me", id=next_message_id).execute()
    parts = next_message["payload"]["parts"]
    text_part = next(part for part in parts if part["mimeType"] == "text/plain")
    b64_body = text_part["body"]["data"]
    body = base64.urlsafe_b64decode(b64_body)
    body = body.decode()
    problem = body.split("----------")[0]
    problem = problem.splitlines()
    if problem[0].lower().startswith("good morning"):
        del problem[0]
    problem_description = "\n".join(problem).strip()

    subject = next(
        head["value"]
        for head in next_message["payload"]["headers"]
        if head["name"] == "Subject"
    )
    match = re.search(r"\[(\w+)\]$", subject)
    if match:
        dificulty = match.group(1)
        lines = problem_description.splitlines()
        lines[0] = f"{lines[0]}\nDificulty: {dificulty}\n\n"
        problem_description = "".join(lines)

    print(problem_description)

    IPython.embed()
    extra_context = {"problem_description": problem_description}
    # cookiecutter("problem_template", extra_context=extra_context)

    # update = messages.modify(userId="me", id=next_message_id,
    #                          body={"removeLabelIds": ["INBOX"]})
    # update.execute()


if __name__ == "__main__":
    main()
