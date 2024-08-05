nums_file = input()

with open(nums_file, "r") as file:
    nums = [int(i.strip()) for i in file.readlines()]

nums.sort()
median = nums[len(nums) // 2]
moves = sum(abs(num - median) for num in nums)

print(moves)
