"""Author - Anantvir Singh, Problem - Leetcode"""

# Reference :- Tushar Roy  -  https://www.youtube.com/channel/UCZLJf_R2sWyUtXSKiKlyvAw

# This is nth Catalan number :   https://en.wikipedia.org/wiki/Catalan_number

def Total_Unique_BST_Possible(n):
    T = [0] * 50                # Size of Table/array can be changed depending on value of n
    T.insert(0,1)
    T.insert(1,1)
    for i in range(2,n+1):      # i=2 to n
        for j in range(i):      # j = 0 to i - 1. j should be less than i
            T[i] = T[i] + T[j] * T[i-j-1]
    return T

print(Total_Unique_BST_Possible(5))






