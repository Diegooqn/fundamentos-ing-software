nums = [4, 1, 9, 6, 3]
target = 10

for i in range(len(nums)):
    for j in range (i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print(nums[i], nums[j])