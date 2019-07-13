"""Problem- Leetcode,  Statement - Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words."""


# O(n^2) ----Not the most efficient solution, but it works well !---- Efficiency can be improved, need to kill the loops earlier(as soon as string is found). They still run completely
def Work_Break(s,wordDict):         # Logic is almost same as matrix chain multiplication. Consider chains of length 2,3,4 .....
    n = len(s) - 1
    tl = []
    for l in range(2,n+1):          # l=2 to n
        for i in range(1,n-l+2):     # i =1 to n-l+1
            j = i+l-1
            print(s[i:j+1])
            if len(wordDict) != 0 and s[i:j+1] in wordDict:
                tl.append(s[i:j+1])
                # https://www.programiz.com/python-programming/methods/string/replace
                s = s.replace(s[i:j+1],"",1)        # Modify the string. Delete the characters/word already found and create a new string. Otherwise results will be inaccurate. Example in "catsandog",if "and" has already been found, then "dog" will be found again because algorithm is still considering chain of length 3. So we should delete "and" once its found in string
                if s == '@':
                    return True
    return False
               
s='@catsandog'
arr = ["cats", "dog", "sand", "and", "cat"]
print(Work_Break(s,arr))
                
