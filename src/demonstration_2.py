"""
You are given a non-empty array that represents the digits of a 
non-negative integer.

Write a function that increments the number by 1.

The digits are stored so that the digit representing the most
significant place value is at the beginning of the array.
 Each element in the array only contains a single digit.

You will not receive a leading 0 in your input array 
(except for the number 0 itself).

Example 1:

Input: [1,3,2]
Output: [1,3,3]
Explanation: The input array represents the integer 132. 132 + 1 = 133.

Example 2:

Input: [3,2,1,9]
Output: [3,2,2,0]
Explanation: The input array represents the integer 3219. 3219 + 1 = 3220.

Example 3:

Input: [9,9,9]
Output: [1,0,0,0]
Explanation: The input array represents the integer 999. 999 + 1 = 1000.
"""

# ! personal attempt (unverified solution)

"""
UNDERSTAND 
given an array with individual numbers comprising a larger solution 
return the next number in the series 
but retain the format of an array with single items 

PLAN 
for the given array, add a zero to the front of the array 
turn into list, 
flip the order 
and add 1 to the first item (0's place)

for i len(list):
    if current >= 10:
        current = current % 10 
        list[i +1] += 1 

reverse this list 

if the first item == 0, remove it 
return the list 
        

"""

# your attempt at the problem 
def plus_one(digits):
    digits.insert(0, 0) # insert 0 at 0 index to compensate for change in signifigance
    rev_list = reversed(list(digits)) #reverse the list 
    print(rev_list)

    rev_list[0] = rev_list[0] += 1 # add one to the 'last' number

    for i in range(len(rev_list)): # for each item in thhe reversed list, check if they are greater than 10
        if rev_list[i] >= 10: 
            rev_list[i] = rev_list[i] % 10 # if so, perform modulo operation, and assign remainder to the item 
            rev_list[i+1] += 1  # and iterate the the next item 
    
    final_list = reversed(rev_list) # reverse the reversed list 

    if final_list[0] == 0: # if the number didn't increase in signifigance, remove the 0
        del final_list[0]
        return final_list
    
    return final_list # return the final answer 

# ! guided attempt 

"""
UNDERSTAND 
given an array with individual numbers comprising a larger solution 
return the next number in the series 
but retain the format of an array with single items 

PLAN 
add one to the last number if it is not a 9,
if it is, add one to the previous number if it is not a 9, 
making the current number, make it a 0 

loop until the current number is not 9:
    if the number is a 9:
        make the current focus a 0, and repeat with previous number 
        set digits[i] to 9
    else if it's not a 9:
        add 1 to the current focus 
if we get to the first number, and it's a 9, make it a 10 
    when we get to index == 0, insert 1 at the 0 index, and make the current focus 0


"""

def plus_one(digits):
    index = len(digits) - 1 #accessing the array starting at the last index 
    while index >= 0 and digits[index] == 9: # if we have digits in the list left AND if the current focus of the loop is a 9 ...
        digits[index] = 0 # assign the current focus to 0 since this is considered a 10 
        index = index - 1 # decremement index tracker after full pass on loop, to iterate to previous (next) item 

    if index == -1:
        digits.insert(0, 1)
    else:
        digits[index] += 1

    return digits 

