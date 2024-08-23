nums = [1, 2, 3, 4, 5, 6]
part1 = nums[:len(nums)//2]
part2 = nums[len(nums)//2:]
result = [part1, part2]
print(result)

nums = [1, 2, 3,]
part1 = nums[:len(nums)-1 //+1]
part2 = nums[len(nums)//-3:]    #[[1, 2], [3]]
result = [part1, part2]
print(result)

nums = []
part1 = nums[:len(nums)//1]
part2 = nums[len(nums)//1:]
result = [part1, part2]
print(result)

