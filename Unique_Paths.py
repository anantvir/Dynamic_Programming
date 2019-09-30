"""Author - Anantvir Singh, Problem - Leetcode, Statement"""

"""Total number of ways to reach every element in 1st row = 1, total number of ways to reach every element in 1st column = 1
=> Total ways to reach cell with index[1][1] i.e P[1][1] = P[0][1] + P[1][0]. Draw on paper to visualize"""


Matrix = [[4,7,3,6],[9,0,1,2],[6,5,9,8],[3,3,8,7]]

def Unique_Paths(M):
    m = len(M)
    n = len(M[0])
    P = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]           # Create same size empty matrix
    for i in range(m):
        for j in range(n):
            P[0][j] = 1                                     # Set 1st column and 1st row = 1
            P[i][0] = 1
    for i in range(m):
        for j in range(n):
            if i > 0 and j > 0:
                P[i][j] = P[i-1][j] + P[i][j-1]             # DP solution
    return P[m-1][n-1]

print(Unique_Paths(Matrix))

    