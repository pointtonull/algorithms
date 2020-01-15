import os
import shutil


TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m [WARNING]: "
INFO = "\x1b[1;33m [INFO]: "
HINT = "\x1b[3;33m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "


def remove_tmp_dir():
    shutil.rmtree("../tmp_{{ cookiecutter.problem_slug }}")


def safe_move(old_path, new_path):
    if os.path.exists(new_path):
        raise RuntimeError("Destination already exists.")
    os.rename(old_path, new_path)


def main():
    filenames = [
            "src/{{ cookiecutter.module_name }}.py",
            "tests/test__{{ cookiecutter.module_name }}.py",
            ]
    for filename in filenames:
        safe_move(filename, "../{}".format(filename))
    remove_tmp_dir()
    print("{}make tdd and happy hacking!{}".format(SUCCESS, TERMINATOR))


if __name__ == "__main__":
    main()
