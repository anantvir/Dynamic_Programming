arr = [None,3,2,2,8,17]

def House_Robber_II(arr):

    n = len(arr)-1
    f_1 = [0]*n
    f_2 = [0]*n
    f_1[1] = arr[1]
    f_1[2] = max(arr[1],arr[2])
    for k in range(3,n):
        f_1[k] = max(f_1[k-2]+arr[k],f_1[k-1])
    
    f_2[1] = arr[2]
    f_2[2] = max(arr[2],arr[3])
    for k in range(3,n):
        f_2[k] = max(f_2[k-2]+arr[k+1],f_2[k-1])
    
    return max(f_1[n-1],f_2[n-1])

print(House_Robber_II(arr))

