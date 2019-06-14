# Storing values into a hash and finding the difference between the target and the elements in the array, if they exist return indicies, else return nothing
if len(nums) < 2:
    return [0, 0]
nums = {nums: idx for idx, nums in enumerate(nums)}

for num1 in nums:
    num2 = target - num1
    if num2 in nums:
        return nums[num1], nums[num2]


## Sort the array, have two different pointers, one at the beginning and the other at the ending. While beginning is less then ending add element at beginning and ending indicies, if greater then target decrement ending, else if less then target incrmenet beginning, else return values at beginning at ending ( This assumes values are found )
# nums.sort()
# beginning = 0
# ending = len(nums) - 1
# while beginning < ending:
#     if nums[beginning] + nums[ending] > target:
#         ending -= 1
#     elif nums[beginning] + nums[ending] < target:
#         beginning += 1
#     else:
#         return [beginning, ending]


## Brute Force Solution, loop through array twice, and find if element at x - target equals any value at array
# for x in range(0, len(nums) ):
#     for y in range(x+1, len(nums)):
#         if nums[y] == target - nums[x]:
#             return [x, y]
