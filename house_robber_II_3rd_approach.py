arr1 = [None,7,2,1,3,4,5,6,3]
arr2 = [None,2,9,1,8,17]
arr = [None,3,2,2,8,17]


def House_Robber_II_New(A):
    n = len(A) - 1
    f = [0]*n           # f(k) denotes total money robbed from houses until k
    if n == 1:
        f[1] = A[1]
    elif n == 2:
        f[2] = A[2]
    elif n == 3:
        f[3] = A[3]
    else:
        V1,V2 = 0,0
        f[1] = A[1]
        f[2] = max(A[1],A[2])
        f[3] = max((f[1]+A[3]),f[2])
        for k in range(4,n):
            f[k] = max((f[k-2]+A[k]),f[k-1])
        V1 = f[n-1]
             
        f[1] = A[2]
        f[2] = max(A[2],A[3])
        f[3] = max((f[1]+A[4]),f[2])
        for k in range(4,n):
            f[k] = max((f[k-2]+A[k+1]),f[k-1])
        V2 = f[n-1]
    return max(V1,V2)



print(House_Robber_II_New(arr))
        
        