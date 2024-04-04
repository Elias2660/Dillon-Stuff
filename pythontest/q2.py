def fib_numbers(length):
    nums = [0, 1]
    if length > 2:
        for index in range(2, length + 1):
            nums.append(nums[index - 2] + nums[index - 1])
    return nums

def draw_fib(length):
    nums = fib_numbers(length)
    string = ""
    for number in nums:
        string += ("*" * number) + "\n"
    return string

print(draw_fib(5))