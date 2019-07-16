"""Problem House Robber II from leetcode"""

#---------------- Not a good approach, Prefer the second approach in next file-----------------

arr = [None,3,2,2,8,17]

def House_Robber_Circular(arr):
    f_k = [0]*len(arr)        # f(k) represents maximum amount robbed from 1st k houses
    n = len(arr) - 1
    first_house_robbed = False
    if n == 1:
        f_k[1] = arr[1]
    if n == 2:
        f_k[2] = max(arr[1],arr[2])
    if n == 3:
        f_k[3] = max(arr[1],arr[2],arr[3])
    else:
        f_k[1] = arr[1]
        f_k[2] = max(arr[1],arr[2])  
        for k in range(3,n+1):
            f_k[k] = max(f_k[k-2]+arr[k],f_k[k-1])
            if f_k[k] == f_k[1]+arr[3]:
                first_house_robbed = True       # If 1st house is robbed, the last cannot be robbed and vice versa
            if first_house_robbed:
                f_k[len(arr)-1] = f_k[len(arr)-2]
    return f_k[n]

print(House_Robber_Circular(arr))
        

         

        