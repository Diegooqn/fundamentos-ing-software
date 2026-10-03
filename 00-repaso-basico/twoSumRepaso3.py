nums = [4, 1, 9, 6, 3]
sumaMayor = nums[0] + nums[1]


for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] > sumaMayor:
            sumaMayor = nums[i] + nums[j]

print(sumaMayor)