import sched
import time


def msleep(milliseconds):
    """MILLISECONDS SLEEP"""
    return time.sleep(milliseconds / 1_000)


SCHEDULER = sched.scheduler(delayfunc=msleep)


def simple_job_scheduler(action: callable, delay: float) -> sched.Event:
    """SIMPLE JOB SCHEDULER

    Args:
        action: a callable
        delay: time to wait until execution, in milliseconds

    Returns:
        A Event handler to allow for this process to be cancelled
    """
    return SCHEDULER.enter(delay, None, action)
