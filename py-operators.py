# Arithmetic Operators
# +, -, *, /, %, **, //

print(10%2) # modulo 0
print(10**2) # power 100
print(10//3) # floor division 3

# Comparison Operators
# ==, !=, >, <, >=, <=
print(10 == 10) # True


# Logical Operators
# and, or, not
print(True and False) # False


# Assignment Operators
# =, +=, -=, *=, /=, %=, **=, //=


# Membership Operators
# in, not in
my_list = [1, 2, 3, 4, 5]
print(3 in my_list) # True


# Identity Operators
# is, is not 
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b) # False
print(a == b) # True
# best use 'if result is None'

# Bitwise Operators
# &, |, ^, ~, <<, >>
def bitwise_operators():
    a = 10  # 1010 in binary
    b = 4   # 0100 in binary

    print(a & b)  # Bitwise AND: 0000 => 0
    print(a | b)  # Bitwise OR: 1110 => 14
    print(a ^ b)  # Bitwise XOR: 1110 => 14
    print(~a)     # Bitwise NOT: -1011 => -11
    print(a << 1) # Left Shift: 10100 => 20
    print(a >> 1) # Right Shift: 0101 => 5

bitwise_operators()
