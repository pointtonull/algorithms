import sched

from pytest import fixture

from src.simple_job_scheduler import simple_job_scheduler, SCHEDULER

"""
SIMPLE JOB SCHEDULER

This problem was asked by Apple.
Difficulty: Medium

Implement a job scheduler which takes in a function f and an integer n, and calls f
after n milliseconds.
"""

CASES = [
    {"values": [5, 3, 3, 4, 0]},
]


@fixture(params=CASES)
def case(request):
    return request.param


def test__simple_job_scheduler__signature(case):
    result = simple_job_scheduler(lambda: 5, 5)
    assert isinstance(result, sched.Event)


def test__simple_job_scheduler__examples(case):
    values = case["values"]
    answer = sorted(values)

    result = []

    for value in values:
        simple_job_scheduler(lambda x=value: result.append(x), value)

    SCHEDULER.run()

    assert answer == result
