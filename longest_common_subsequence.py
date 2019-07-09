"""Author - Anantvir Singh, concept reference:= CLRS, Dynamic Programming page 393"""

#---------------------------Bottom-up Approach-----------------------------------

# inputs are 2 sequences X and Y of length m and n respectively. c[i][j] is length of LCS of sequences of length X_i and Y_j
# Refer to CLRS page 393 for detailed explanation behind the recursive formula

def Longest_Common_Subsequence(X,Y):
    m = len(X)
    n = len(Y)
    c = [[0 for x in range(n)]for x in range(m)]
    b = [[0 for x in range(n)] for x in range(m)]
    
    for i in range(1,m):
        c[i][0] = 0
    for j in range(1,n):
        c[0][j] = 0
    for i in range(1,m):
        for j in range(1,n):
            if X[i] == Y[j]:
                c[i][j] = 1 + c[i-1][j-1]
                b[i][j] = 'Diagnol'
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = 'Up'
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = 'Left'
    return c,b

X = [None,'A','B','C','B','D','A','B']      # We can increase all indices by 1 if we dont want to add None at the beginning of arrays X and Y, (Trivial)
Y = [None,'B','D','C','A','B','A']      
print(Longest_Common_Subsequence(X,Y))

