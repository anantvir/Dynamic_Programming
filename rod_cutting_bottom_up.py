"""Author - Anantvir Singh, concept reference:= CLRS"""

# Using buttom up approach for Dynamic Programming.
# This approach starts calculating solution from smallets possible cases. Example, a rod of length 1 inch will generate a revenue
# p[1] = r[1] where p[i] = price of i inches of rod and r[i] = revenue from i inches of rod
# Similarly for 2 inches of rod, revenue can be maximized by choosing max of ( p[1] + r[1] or p[2] + r[0])
# Similarly for 3 inches of rod, revenue can be maximized by choosing max of ( p[1] + r[2] or p[2] + r[1],p[3] + r[0])
# Similarly for 3 inches of rod, revenue can be maximized by choosing max of ( p[1] + r[3] or p[2] + r[2],p[3] + r[1],p[4] + r[0]) and so on !


def Rod_Cutting_Bottom_Up(p,n):             # n = length of rod, p = array of prices for each inch
    r = []
    r.insert(0,0)                           # r[0] = 0, because no revenue generated from rod of length zero !
    for j in range(1,n+1):
        q = -10000000000
        for i in range(1,j+1):
            q = max(q, p[i] + r[j-i])
        r.insert(j,q)
    return r[n]

arr = [None,1,5,8,9,10,17,17,20,24,30]

print(Rod_Cutting_Bottom_Up(arr,7))