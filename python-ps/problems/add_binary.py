def add_binary(a: str, b: str) -> str:
    return bin(int(a, 2) + int(b, 2))[2:]

if __name__ == "__main__":
    a = "11"
    b = "1"
    print(add_binary(a, b))