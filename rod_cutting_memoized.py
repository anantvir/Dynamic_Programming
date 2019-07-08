"""Author - Anantvir Singh, concept reference:= CLRS"""

# We introduce memoization-- which means store already computed values and refer to them when you need the same value again
# If its already in storage, then use that value otherwise compute the value and store it or memoize it

def Memoized_Rod_Cutting(P,n):           # n = length of rod, P = array of prices for each inch
    Memo = []                            # create array to store calculated values for future reference
    for i in range(n+1):
        Memo.insert(i,-1)                # Revenue should always be +ve, so -1 means the value has not been computed yet
    return Memoized_Rod_Cutting_Aux(P,n,Memo)

def Memoized_Rod_Cutting_Aux(P,n,Memo):
    if Memo[n] >= 0:                     # check if revenue for rod of length n exists in memoized array ?
        return Memo[n]                          
    if n == 0:                           
        return 0
    else:
        q = -10000000000                 # -ve infinity
        for i in range(1,n+1):
            q = max(q, P[i] + Memoized_Rod_Cutting_Aux(P,n-i,Memo))
    
    """-------------------Memoization Step-----------------------"""
    Memo[n] = q                                                         # Store in array after calculation if this value doesnt exist already
    return q

arr = [None,1,5,8,9,10,17,17,20,24,30]

print('Answer :',Memoized_Rod_Cutting(arr,4))
