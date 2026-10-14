
from collections.abc import Iterable, Iterator

# List of backend logs
logs = [
    "INFO: User logged in",
    # "ERROR: Database connection failed",
    "INFO: Request completed",
    # "ERROR: Payment failed",
    # "ERROR: Payment failed",
    "WARNING: Response time is high",
]

# Generator: yield errors one by one
def get_errors(logs: Iterable[str]) -> Iterator[str]:
    if logs is None:
        raise ValueError("Logs cannot be None")
    for log in logs:
        # Check whether the log level is exactly ERROR
        if log.split(":")[0] == "ERROR":
            yield log

# Exaract Error message
def extract_error_message(logs):
    for log in logs:
        error = log.split(":")[1].strip()
        yield error


# Count how many logs belong to each level
def count_levels(logs: Iterable[str]) -> dict[str, int]:
    counts = {}

    for log in logs:
        # Extract the level before the colon
        level = log.split(":")[0]

        # Frequency counting using a dictionary
        counts[level] = counts.get(level, 0) + 1

    return counts

def count_error_types(messages):
    if messages is None:
        raise ValueError("Messages cannot be None")

    counts: dict[str, int] = {}

    for msg in messages:
        key = msg
        if key in counts:
            counts[key] += 1
        else:
            counts[key] = 1
    return counts

# Analyze logs in a single pass
def analyze_logs(logs: Iterable[str]) -> dict[str, int]:
    if logs is None:
        raise ValueError("Logs cannot be None")
    counts = {}

    print("All Errors:")

    for log in logs:
        level = log.split(":")[0]

        # Count the current log level
        counts[level] = counts.get(level, 0) + 1

        # Print errors immediately
        if level == "ERROR":
            print(log)

    print("\nLog Counts:")
    print(counts)

    return counts

# Program entry point
if __name__ == "__main__":
    errors = get_errors(logs)
    messages = extract_error_message(errors)
    result = count_error_types(messages)

print(result)

# Software Engineer Joseph.