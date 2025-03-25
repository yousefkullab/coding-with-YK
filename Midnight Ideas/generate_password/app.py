import random

def generate_password(lenght):
    password = ''
    for i in range(lenght):
        x = chr(random.randint(0, 25)+97)
        password += x
        
    return password


print(generate_password(100))