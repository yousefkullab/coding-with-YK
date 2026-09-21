# Undersrand 
#   * inptu arr of temps
#   * output arr of days you have wait to after i th 
#   * if there is no future day keep it 0

# Middle Example 
#   temperatures = [73,74,75,71,69,72,76,73]
#   [1,1,4,2,1,1,0,0]

# Brute Force, Time O(n*2), Space O(n)
class Solution:
    def dailyTemperatures(self, temps):
        res = []
        for i in range(len(temps)):
            for j in range(i+1, len(temps)):
                if temps[j] > temps[i]:
                    res.append(j-i)
                    break
            else:
                res.append(0)
        return res
    
# print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))

# Problem > We Know the temp greather than other but still check

# Optimize > Use Monotonic Stack 

# code
class Solution:
    def dailyTemperatures(self, temps):
        stack = []
        res = [0] * len(temps)

        for i, temp in enumerate(temps):
            while stack and temps[stack[-1]] < temp:
                previous = stack.pop()
                res[previous] = i-previous
            stack.append(i)
        return res

# Test & Complexity Time O(n), Space O(n)

if __name__ == '__main__':

    s = Solution()
    print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))

    
