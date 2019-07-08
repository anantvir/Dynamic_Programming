r = 3
c = 3

A = [[2 for x in range(r)] for x in range(c)]
B = [[3 for x in range(r)] for x in range(c)]

def Square_Multiply(A,B):
    if len(A[0]) != len(B):
        raise ValueError('Columns of A not equal to rows of B !')
    else:
        C = [[0 for x in range(len(A))] for x in range(len(B[0]))]
        for i in range(len(A)):
            for j in range(len(B[0])):
                C[i][j] = 0
                for k in range(len(A[0])):
                    C[i][j] = C[i][j] + A[i][k]*B[k][j]
    return C

print(Square_Multiply(A,B))
