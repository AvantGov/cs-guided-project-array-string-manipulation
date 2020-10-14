"""
Given an array of integers `nums`, define a function that returns the "pivot" index of the array.

The "pivot" index is where the sum of all the numbers on the left of that index is 
equal to the sum of all the numbers on the right of that index.

If the input array does not have a "pivot" index, then the function should 
return `-1`. If there are more than one "pivot" indexes, then you should return the 
left-most "pivot" index.

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The sum of the numbers to the left of index 3 (1 + 7 + 3 = 11) is equal to the sum of 
numbers to the right of index 3 (5 + 6 = 11).
Also, 3 is the first index where this occurs.

Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
"""


"""
UNDERSTAND
we want to return the index of the number that will
we want to return the first intance of this, so when it is foudn we do not
need to continue the operation 

we do not need to include the current index in the comparison sums 


PLAN 
if the list is empty, return nothing 
if the list has a length of one, return -1 as the result 

create left_comp
create right_comp 

iterate through the array:
    for each index in the list 
    sume the left and right items in the list 
    compare 
        if equal, stop the loop and return the current index 


"""

def pivot_index(nums):
    for i in range(len(nums)):
        left_comp = sum(nums[0:1])
        right_comp = sum(nums[i+1:])
        if left_comp == right_comp:
            return i
            break
    return "nothing found"

"""
There is a more efficient method of approaching this by keeping a running total 
that can be constantly used as a comparison 

PLAN II
create left_comp 
iterate through the array 
    add nums[i] to left_comp 
    iterate through the array from the end of teh array and work back towards 1

in order for this to function properly, it would be best to remove the current
item from the group on the beginning of each iteration
so that the comparison can happen accurrately without consideration of the 
current index 



"""

# II 
def pivot_index(nums):
    if len(nums) <= 1:
        return -1
    
    left_comp = 0
    right_comp = sum(nums)

    for i in range(len(nums)):
        right_comp -= nums[i]
        if left_comp == right_comp:
            return i 
            break 
        left_comp += nums[i]
        continue

    return -1

"""
PLAN  III
left = 0 
right = sum of the entire array 
iterate through the array 
    add nums[i] to left_comp 
    right side = sum of the entire array - left_comp - nums[i]


"""
def pivot_index(nums):
