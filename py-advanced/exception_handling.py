# try, except, else, finally

try:
    number = int("Hello")
except ValueError:
    print("Invalid number")

else:
     print("Conversion successful")
finally:
    print("Operation finished")

# Custom Exception ( Best Practice )
class InvalidLogFormatError(Exception):
    pass

def check_format(log_format):
    formats = ["json", "text"]

    if log_format not in formats:
        raise InvalidLogFormatError(
                f"Unsupported format: {log_format}. "
                "Supported formats: json, text"
)
    return True

try:
    log_format = check_format("xml")
except InvalidLogFormatError as e:
    print(e) 
