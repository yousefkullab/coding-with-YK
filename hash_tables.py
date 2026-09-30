users = {
    "yousef": 24,
    "Ali": 22,
    "mina": 20
}

# Access / Lookup ( Complexity Avg O(1) )
age = users["yousef"] # users.get("yousef") if not found return None
print(age)

# Insert ( Complexity Avg O(1) )
users["omar"] = 23 # Note if the key is exist the value will updated
print(users)

# Delete ( Complexity Avg O(1) )
del users["Ali"] # you can also use pop()
print(users)

# Search  Complexity Avg O(1))
if "yousef" in users:
    print("Found")

# Note: A set is also hash-table based and is excellent for existence/duplicate checking.

