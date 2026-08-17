import pandas as pd
import re
import csv

# This function convert excel to csv file and It returns values of a specified pattern
def excel_to_list(excel_file, pattern):
    data = pd.read_excel(excel_file)  
    new_data = data.to_csv()
    with open("output.csv", "w", newline="") as file:
        file.write(new_data)
    Phones = []
    with open("output.csv", "r") as file:
        for line in file:
            Phones += re.findall(pattern, line)
    return Phones
    

file = "Book.xlsx"
pattern = r"\d\d\d\d\d\d\d\d\d"
Phones = excel_to_list(file, pattern)
print(Phones)


# Software Engineer Joseph.
