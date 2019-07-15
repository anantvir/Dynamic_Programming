"""Problem- Leetcode, statement = House Robber"""

arr = [None,2,7,9,3,1]

def Rob_Houses_With_Max_Amount(arr):
    f_k = [0]*len(arr)  
    for k in range(1,len(arr)):
        if k==1 or k==2:
            f_k[0] = 0
            f_k[-1] = 0
        f_k[k] = max(f_k[k-2]+arr[k],f_k[k-1])
    
    return f_k[len(arr)-1]
        
        
print(Rob_Houses_With_Max_Amount(arr))