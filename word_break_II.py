"""Problem - Leetcode, Statement - Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences."""
# Reference - https://www.geeksforgeeks.org/

s= 'catsanddog'
wd = ["cat", "cats", "and", "sand", "dog"]
found_list = []

result = ""
stack = []
def Word_Break_II(s,wd,result,found_list):
    n = len(s)
    for i in range(1,n+1):          # Start from left end of string, when a word is found in 'wd', then trim the string and recursively call the function
        if s[0:i] in wd:
            if i == n:
                result += s[0:i]
                print('Result is :',result)
                return result 
            Word_Break_II(s[i:n],wd,result+s[0:i]+" ",found_list)

Word_Break_II(s,wd,result,found_list)








# stack = []
# def Word_Break_II(s,wd):
#     wd.sort(key=len)
#     if len(s) == 0:
#         print('Stack')
#     if len(s) < len(wd[0]):
#         stack.pop()
#     n = len(s) - 1
#     for l in range(1,n+1):
#         for i in range(1,n-l+2):
#             j = i + l - 1
#             print(s[i:j+1])
#             if s[i:j+1] in wd:
#                 stack.append(s[i:j+1])
#                 Word_Break_II(s.replace(s[i:j+1],"",1),wd)
            

# Word_Break_II(s,wd)






