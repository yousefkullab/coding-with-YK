from collections.abc import Iterable, Iterator
from core.exceptions import InvalidLogInputError

# Generator: yield errors one by one
def get_errors(logs: Iterable[str]) -> Iterator[str]:
    if logs is None:
        raise InvalidLogInputError("Logs cannot be None")
    for log in logs:
        # Check whether the log level is exactly ERROR
        if log.split(":")[0] == "ERROR":
            yield log

# Exaract Error message
def extract_error_message(logs):
    if logs is None:
        raise InvalidLogInputError("Logs cannot be None")
    for log in logs:
        msg = log.split(":")[1].strip()
        yield msg.strip()
