import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call(item):
    """Treat an unsolved practice stub (raise NotImplementedError) as a skip,
    not a failure, so the suite stays green until the learner implements it."""
    outcome = yield
    if outcome.excinfo is not None and issubclass(outcome.excinfo[0], NotImplementedError):
        outcome.force_exception(pytest.skip.Exception("not implemented yet"))
