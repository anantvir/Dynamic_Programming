"""Problem - Leetcode, Statement  - Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product."""

nums = [-5,-10,0,5,7,6]

def Maximum_Product_Subarray(nums):
    n = len(nums)
    result = float("-inf")
    
    for i in range(n):
        curr_prod = max_prod = nums[i]
        for j in range(i+1,n):
            curr_prod = curr_prod * nums[j]
            max_prod = curr_prod if curr_prod > max_prod else max_prod
        result = max_prod if max_prod>result else result
    return result

print(Maximum_Product_Subarray(nums))

