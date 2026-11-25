import re

# Python Regex Cheatsheet https://www.debuggex.com/cheatsheet/regex/python
# Used to search, match, extract, and replace text patterns.
# Used In Cradit card validation, IP Address Validation, Email Validation, ....
# r > Raw String make writing Regex patterns easier.


# search()   > search anywhere in the sting and return first pattern
# match ()   > checkes only the beginning 
# findall    > return all mathces
# sub()      > replace strings
# split()    > split sting used pattern
# compile () > change regex pattern to object
# finditer() > find all and return mathces objects as iterator insted of list of string


log = "ERROR: User 125 failed login"
result = re.search(r"(\w+): User (\d+)", log)
if result:
    print(result)
    print(result.string)
    print("Start position:", result.start())
    print("End position:", result.end())
    print("Matched span:", result.span())
    print("Matched text:", result.group(0))
    print("Matched text:", result.group(1))
    print("Matched text:", result.group(2))

print("#" * 100)

new_result = re.sub("ERROR", "INFO", log)
print(new_result)
new_result = re.split(r":", log)
print(new_result)

print("#" * 100)

logs = [
    "INFO: User logged in",
    "ERROR: Database failed",
    "ERROR: Payment failed",
]
error_pattern = re.compile(r"ERROR")
for log in logs:
    if error_pattern.search(log):
        print(log)

print("#" * 100)

text = "User 123 failed. User 456 failed."
for match in re.finditer(r"\d+", text):
    print("Value:", match.group())
    print("Position:", match.span())

# --- Character Classes
# \d - Mathces digits (0-9)
# \w - Mathces letters, digits, underscore
# \s - Mathces whitespace
# [A-Z] - Mathces uppercase english letters
# [a-z] - Mathces lowercase english letters
# [0-9] - Mathces digits 
# [A-Za-z] - Mathces uppercase and lowercase letters

# --- QUANTIFIERS
# + means one or more occurrences
# * means zero or more occurrences
# ? means zero or one occurrences
# {n} means Exactly n occurrences
# {n, m} means bettween n and m occurrences

# --- Anchors
# ^ Mathces the beginnig of the string
# $ Mathces the end of aresult = re.search(r"(\w+): User (\d+)", log)

# () Captuing Groups
# (?:...) Non-Capturing Groups


