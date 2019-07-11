"""Author - Anantvir Singh, Problem - Leetcode"""

"""Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000."""


# --------------------------- Dynamic Programming, Bottom-Up Approach ----------------------------------------------

s ='@dbdadbdaaadbdaa'

#arr = [[],[],[]]

# arr[1].append(s[8:9+1])
# print(arr)

def Longest_Palindrome_Substring(s):
    arr=[[-1]]*len(s)
    # print(id(arr[1]))
    # print(id(arr[2]))
    # print(id(arr[3]))
    arr.insert(0,None)
    n = len(s)-1
    #arr[2] = []
    for l in range(2,n+1):
        for i in range(1,n-l+2):
            j = i+l-1
            if l == 2:
                if s[i] == s[j]:
                    print(arr[2][0])
                    #arr[2].pop()
                    arr[2][0].append(s[i:j+1])
            else:
                sub = j-i-1
                if s[i+1:j] in arr[sub] and s[i] == s[j]:
                    arr[l] = s[i,j+1]
    return arr
    
Longest_Palindrome_Substring(s)



