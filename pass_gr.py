# import sting, random modules
# store all characters in lists (upper/lower case, digits, punctuations)
# the number of characters from user
# make sure the number of characters is 6 or more
# shuffle all lists
# calculate 30% and 20% of number of characters
# create password 60% letters and 40% digits and punctuations

import string, random

upper_list = list(string.ascii_uppercase)
lower_list = list(string.ascii_lowercase)
digit_list = list(string.digits)
punctuation_list = list(string.punctuation)

character_len = input("How many character for the password: ")

while True:

    try:
        
        character_len = int(character_len)
        
        if character_len < 6:
            print("try again you need at least 6 characters")
            character_len = input("Please enter the number again: ")
        else:
            break
    except:
        
        print("Please enter a number only")
        character_len = input("How many character for the password: ")


random.shuffle(upper_list)
random.shuffle(lower_list)
random.shuffle(digit_list)
random.shuffle(punctuation_list)


part1 = round(character_len * (30/100))
part2 = round(character_len * (20/100))

password = []

for i in range(part1):
    password.append(upper_list[i])
    password.append(lower_list[i])

for i in range(part2):
    password.append(digit_list[i])
    password.append(punctuation_list[i]) 
    
random.shuffle(password)

password = "".join(password[:])

print(f"The Password: {password}")

# Software Engineer Joseph .