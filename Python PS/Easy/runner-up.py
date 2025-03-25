# Find the Runner-Up Score!
# runner-up >>> the competitor that does not win first place in a contest. especially : one that finishes in second place.

# you give the n scores and store them in list and find the runner-up score

# constraints 
# 2 <= n <= 10
# -100 <= A[i] <= 100  # A[] >>> array of n integers 

if __name__ == '__main__':
    n = int(input("n: "))
    arr = map(int, input("Array: ").split())
    list_scores = list()
    for i in arr:
        list_scores.append(i)
    list_scores.sort(reverse=True)
    set_of_scores = set()
    for i in list_scores:
        set_of_scores.add(i)
    # print(set_of_scores)
    sorted_set = sorted(set_of_scores, reverse=True)
    # print(sorted_set)
    runner_up = sorted_set[1]
    print(f"the runner_up is: {runner_up}")
