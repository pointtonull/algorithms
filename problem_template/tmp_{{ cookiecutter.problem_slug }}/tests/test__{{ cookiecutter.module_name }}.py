from pytest import fixture

from {{ cookiecutter.module_name }} import {{ cookiecutter.function_name }}
from .utils import deep_diff

"""
{{ cookiecutter.problem_name}}

{{ cookiecutter.problem_description }}
"""

CASES = [
    {
        "input1": 1,
        "input2": 2,
        "answer": 3,
    },
    {
        "input1": 2,
        "input2": 2,
        "answer": 4,
    },
    {
        "input1": 4,
        "input2": -2,
        "answer": 2,
    }
]



@fixture(params=CASES)
def case(request):
    return request.param


def test__{{ cookiecutter.function_name }}__signature(case):
    input1 = case["input1"]
    input2 = case["input2"]

    result = {{ cookiecutter.function_name }}(input1, input2)
    assert isinstance(result, list)

    result = {{ cookiecutter.function_name }}(input1, input2)
    assert isinstance(result, int)


def test__{{ cookiecutter.function_name }}__examples(case):
    input1 = case["input1"]
    input2 = case["input2"]
    answer = case["answer"]

    result = {{ cookiecutter.function_name }}(input1, input2)
    assert not deep_diff(answer, result)
