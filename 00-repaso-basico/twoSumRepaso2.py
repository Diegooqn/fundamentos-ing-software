nums = [1, 3, 5, 3, 8]

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            print(nums[i], nums[j])