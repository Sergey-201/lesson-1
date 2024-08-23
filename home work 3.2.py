nums = [12, 3, 4, 10]
nums.insert(0, nums[-1])
nums.pop()
print(nums)

nums = [1]
nums.insert(0, nums[-1])
nums.pop()
print(nums)

nums = []
nums = nums[-1] if nums else nums
print(nums)



