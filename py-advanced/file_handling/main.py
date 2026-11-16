# file mode
#   - r > read
#   - w > write 
#   - a > append
#   - x > create if not exist
#   - rb > read binary file
#   - wb > write binary file


with open("py-advanced/file_handling/app.log", "r") as file:
    for line in file:
        print(line)
# read() read all file and return str
# readline() read one line
# readlines() read all lines and return list of str lines

# Absolute Path > all path form root /
# Relative Path > all path form Current Working Directory

# JSON : JavaScript Object Notation

import json

report = {
    "total_logs": 100,
    "errors": 15,
    "warnings": 20,
}
# 
json_data = json.dumps(report, indent=4)

print("JSON data\n", json_data)

# Function	Input	                 Output
# dumps()	Python Object	         JSON String
# dump()	Python Object + File	 Wirte JSON in File
# loads()	JSON String	             Python Object
# load()	File	                 Python Object

