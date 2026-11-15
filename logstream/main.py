
from services.log_filter import get_errors, extract_error_message
from core.exceptions import LogStreamError

from services.log_analyzer import (
    count_levels,
    count_error_types,
    analyze_logs,
)
# List of backend logs
logs = [
    "INFO: User logged in",
    "ERROR: Database connection failed",
    "INFO: Request completed",
    "ERROR: Payment failed",
    "ERROR: Payment failed",
    "WARNING: Response time is high",
]

# Program entry point
if __name__ == "__main__":
    try:
        analyze_logs(logs)
    except LogStreamError as e:
        print(e)

# Software Engineer Joseph.