
def isValid(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        # push the opening parentheses on to stack
        if char in mapping.values():
            stack.append(char)
        
        else:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
    return len(stack) == 0

if __name__ == "__main__":    
    s = "({}())"
    print(isValid(s))