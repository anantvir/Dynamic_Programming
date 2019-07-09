"""Author - Anantvir Singh, concept reference:= CLRS, Dynamic Programming page 370"""

#---------------------------Bottom-up Approach-----------------------------------

def Matrix_Chain_Multiplication(p):
    n = len(p) - 1
    m = [[0 for x in range(n+1)] for x in range(n+1)]       # To keep the program simpler m[0][x] row and m[x][0] column are unused 
    s = [[0 for x in range(n+1)] for x in range(n+1)]       # To keep program simpler s is same size as m. Ideally should be of size s[1..n-1][2..n]
    for i in range(1,n+1):
        m[i][i] = 0                             # Multiplication of matrix with itself needs zero multiplications

    for l in range(2,n+1):                      # Length of chain to be considered
        for i in range(1,n-l+2):
            j = i + l -1                        # i and j are calculated according to length of chain considered. Example for l=3, if i=1 then j=3 which represents multiplication of matrices A1,A2,A3,if i=2 then j=4 which is A2*A3*A4,if i=3 then j=5 which is A3*A4*A5 and so on.. 
            m[i][j] = 10000000000000            # +ve infinity
            for k in range(i,j):
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]      # Optimal sub structure
                if q < m[i][j]:
                    m[i][j] = q                 # if q decreases further, then update it in table
                    s[i][j] = k                 # s table is to build the final solution.(Trivial)
    return m[1][n],s

arr = [5,4,6,2,7]


print('Minimum Number of scalar multiplications required :',Matrix_Chain_Multiplication(arr)[0])
