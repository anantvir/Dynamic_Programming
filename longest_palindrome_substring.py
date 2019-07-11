"""Author - Anantvir Singh, Problem - Leetcode"""

"""Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000."""


# --------------------------- Dynamic Programming, Bottom-Up Approach ----------------------------------------------

s ='@dbdadbdaaadbdaa'                               # 1st character is a random special character to keep the problem simple as its easier to handle for indices starting from 1

def Longest_Palindrome_Substring(s):
    dic={}                                          # IMPORTANT !! -->>> Create empty dict/hashtable. Do not create list of lists. For some reason, if we create dict of dicts like arr = [[]]*len(s) then all the dictionaries created inside the outer dict i.e arr[1],arr[2],arr[3] and so on are pointing to the same object(a single dict object). So if we make a change to once index, then its changed in the entire array. Its explained in the below commented code
    for i in range(1,len(s)):
        dic[i] = []
    dic[0] = None
    for j in range(1,len(s)):
        dic[1].append(s[j])
    n = len(s)-1
    for l in range(2,n+1):                          # Same strategy as Matrix Chain Multiplication
        for i in range(1,n-l+2):
            j = i+l-1
            if l == 2:
                if s[i] == s[j]:                    # for length 2, if 1st element = 2nd then appen it to secind index of dict
                    dic[2].append(s[i:j+1])
            else:
                sub = j-i-1
                if s[i+1:j] in dic[sub] and s[i] == s[j]:
                    dic[l].append(s[i:j+1])         # Else, for example for l=5, check if s[i+1,j-1] is already stored in our dict at index sub = j-i-1. It will be stored bevause we are building a bottom up approach
    return dic

Longest_Palindrome_Substring(s)                     # Returns a dict. Now we just have to resturn the key whose value has maximum length (Trivial !)


"""Here we create list of lists, hence arr[1],arr[2],arr[3] .... all point to same list object. Change in 1 causeswhole list to change"""
# def Longest_Palindrome_Substring(s):
#     arr=[[-1]]*len(s) 
#     # print(id(arr[1]))
#     # print(id(arr[2]))
#     # print(id(arr[3]))
#     arr.insert(0,None)
#     n = len(s)-1
#     #arr[2] = []
#     for l in range(2,n+1):
#         for i in range(1,n-l+2):
#             j = i+l-1
#             if l == 2:
#                 if s[i] == s[j]:
#                     print(arr[2][0])
#                     #arr[2].pop()
#                     arr[2].append(s[i:j+1])           
#             else:
#                 sub = j-i-1
#                 if s[i+1:j] in arr[sub] and s[i] == s[j]:
#                     arr[l] = s[i,j+1]
#     return arr



