# dict >>> key, value paris

# get, update, pop, clear, .keys(), .values(), .items(), len()
# Dictionary Keys Must Be Hashable keys can be number, tuple, str but can not be list

# DICT
# Lookup       O(1) average
# Insert       O(1) average
# Delete       O(1) average

user = {
    "name": "yousef",
    "age": 24,
    "email": "yousef.kh.kullab@gmail.com"
}

print(user["email"]) # access
print(user.get("name"))
print(user.get("grade", "Not provied"))

user["grade"] = 88
print(user)

for k, v in user.items():
    print(f"{k} > {v}")

 