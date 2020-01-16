def {{ cookiecutter.function_name }}(input1, input2):
    """{{ cookiecutter.problem_name}}

    {{ cookiecutter.problem_description }}
    """
    result = []
    raise NotImplementedError("Must implement {{ cookiecutter.problem_name }} solution.")
    return result


if __name__ == "__main__":
    print({{ cookiecutter.function_name}}())
