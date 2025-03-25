# String Validators

if __name__ == '__main__':
    s = input("s: ")  

    print(True in list(map(lambda n:n.isalnum(), s)))
    print(True in list(map(lambda n:n.isalpha(), s)))
    print(True in list(map(lambda n:n.isdigit(), s)))
    print(True in list(map(lambda n:n.islower(), s)))
    print(True in list(map(lambda n:n.isupper(), s)))
    
