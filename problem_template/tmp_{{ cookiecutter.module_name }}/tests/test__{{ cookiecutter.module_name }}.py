from pytest import fixture

from src.{{ cookiecutter.module_name }} import {{ cookiecutter.function_name }}

"""
{{ cookiecutter.problem_name.upper() }}

{{ cookiecutter.problem_description }}
"""

CASES = [
    {
        "input1": 1,
        "answer": 3,
    },
    {
        "input1": 2,
        "answer": 4,
    },
    {
        "input1": 4,
        "answer": 2,
    }
]



@fixture(params=CASES)
def case(request):
    return request.param


def test__{{ cookiecutter.function_name }}__signature(case):
    input1 = case["input1"]

    result = {{ cookiecutter.function_name }}(input1)
    assert isinstance(result, int)


def test__{{ cookiecutter.function_name }}__examples(case):
    input1 = case["input1"]
    answer = case["answer"]

    result = {{ cookiecutter.function_name }}(input1)
    assert answer == result

