"""Author - Anantvir Singh, concept reference:= CLRS, Dynamic Programming page 370"""

#---------------------------Memoization Approach-----------------------------------
import math
def Matrix_Chain_Memoized(p):
    n = len(p) - 1
    m = [[0 for x in range(n+1)]for x in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            m[i][j] = math.inf
    return Matrix_Chain_Lookup(p,m,1,n)

def Matrix_Chain_Lookup(p,m,i,j):
    if m[i][j] < math.inf:
        return m[i][j]
    if i == j:
        m[i][j] = 0             # no cost of multiplying single matrix with itself
    else:
        for k in range(i,j):
            q = Matrix_Chain_Lookup(p,m,i,k) + Matrix_Chain_Lookup(p,m,k+1,j) + p[i-1]*p[k]*p[j]
            if q < m[i][j]:
                m[i][j] = q
    return m

arr = [5,4,6,2,7]
print(Matrix_Chain_Memoized(arr))