logs = [
    "INFO: User logged in",
    "ERROR: Database connection failed",
    "INFO: Request completed",
    "ERROR: Payment failed",
    "WARNING: Response time is high",
]

from collections.abc import Iterable, Iterator

# handle error error when found it insted of return all list of error this good with a big data
def get_errors(logs:Iterable[str]) -> Iterator[str]:
    for log in logs:
        if "ERRORS" in log:
            yield logs


