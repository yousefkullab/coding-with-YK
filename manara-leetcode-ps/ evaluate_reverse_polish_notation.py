# Understand 
# input: arry of string tokens represents an arthimetic expressions in Reverse Polish Notation.
# output: Evaluate the expression and return the integer result.
# Constraints: tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].

# Midd Example 
# tokens = ["2","1","+","3","*"]
# Output: 9

# Brute Force Time O(n^2), Space O(n)
# pseudocode
#   search for operator and the operands that connected with it
#   cal the res
#   repalce the process with res
#   loop until stay one number 

# Problem > when replace the process it loop for all array again 

# Optimize > use Stack Last-In-First-Out 

# Code
class Solution:
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if token not in ["*", "-", "/", "+"]:
                token = int(token)
                stack.append(token)
            else:
                right = stack.pop()
                left = stack.pop()

                if token == "+":
                    stack.append(left + right)
                
                elif token == "-":
                    stack.append(left - right)
                    
                elif token == "*":
                    stack.append(left * right)
                    
                elif token == "/":
                    stack.append(int(left / right))

        return stack[0]
                    

# Test & Complexity Time O(n), Space O(n)

s = Solution()
print(s.evalRPN(["5","1","+","3","*"]))
print(s.evalRPN(["2","1","+","3","*"]))
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

