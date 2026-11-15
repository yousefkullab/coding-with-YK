from collections.abc import Iterable
from core.exceptions import InvalidLogInputError

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
        raise InvalidLogInputError("Messages cannot be None")

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
        raise InvalidLogInputError("Logs cannot be None")
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