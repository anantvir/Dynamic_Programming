

arr = [None,9,2,1,8,8,5,6]

def House_Robber_II_IV(A):
    n = len(A) - 1
    f = [0] * len(A)
    f[1] = A[1]
    f[2] = max(A[1],A[2])
    f[3] = max(f[2],(f[1]+A[3]))#--------------------->>>>>> Wrong logic !!!!!!!!! f[3] cant tell anything !!
    First_Rob = None
    if f[3] == f[1]+A[3]:
        First_Rob = True
    else:   
        First_Rob = False
    

