"""Author - Anantvir Singh, Problem - Leetcode, Statement - Perfect Squares, Problem Number -279"""

"""------------------------------------ Bottom Up Memoization Approach ------------------------------------"""

import math

n = 12
p = [1,4,9,16,25,36,49,64]
arr = [math.inf]*(n+1)
arr[0] = 0                  # 0 number of perfect squares required to represent 0
arr[1] = 1                  # 1 number of perfect squares required to represent 1. i.e 1 can be represented as 1^2

def Perfect_Squares(n,p):
    m = len(p)
    for i in range(2,n+1):
        for j in range(m):
            if p[j] < n:        # If the perfect square is less than our number 'n'
                d = i - p[j]
                r = 1 + arr[d]  # One perfect square has been considered for sure. So add 1 to sum and subtract it from n. The see the remaining number in arr[remaining number]
                if r < arr[i]:
                    arr[i] = r
            else:
                break
    return arr[n]

print(Perfect_Squares(n,p))