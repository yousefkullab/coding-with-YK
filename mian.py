
from collections.abc import Iterable, Iterator

# List of backend logs
logs = [
    "INFO: User logged in",
    "ERROR: Database connection failed",
    "INFO: Request completed",
    "ERROR: Payment failed",
    "WARNING: Response time is high",
]

# Generator: yield errors one by one
def get_errors(logs: Iterable[str]) -> Iterator[str]:
    for log in logs:
        # Check whether the log level is exactly ERROR
        if log.split(":")[0] == "ERROR":
            yield log


# Count how many logs belong to each level
def count_levels(logs: Iterable[str]) -> dict[str, int]:
    counts = {}

    for log in logs:
        # Extract the level before the colon
        level = log.split(":")[0]

        # Frequency counting using a dictionary
        counts[level] = counts.get(level, 0) + 1

    return counts


# Analyze logs in a single pass
def analyze_logs(logs: Iterable[str]) -> dict[str, int]:
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
    analyze_logs(logs)
