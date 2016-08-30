
nums = [1, 5, 6, 7, 6, 6, 7, 4, 6, 7, 7]
while (6 in nums):
    del nums[nums.index(6):nums.index(7)+1]
print nums
