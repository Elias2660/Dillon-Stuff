def fib_numbers(length):
    nums = [0, 1]
    if length > 2:
        for index in range(2, length + 1):
            nums.append(nums[index - 2] + nums[index - 1])
    return nums

print(fib_numbers(3))