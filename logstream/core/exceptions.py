class LogStreamError(Exception):
    pass

class InvalidLogInputError(LogStreamError):
    pass

class InvalidLogFormatError(LogStreamError):
    pass

class LogNotFoundError(LogStreamError):
    pass