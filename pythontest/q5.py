def find_mode(nums):
    freq = {}
    cur_num, cur_max = 0, 0
    for num in nums:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1
        if freq[num] > cur_max:
            cur_max = freq[num]
            cur_num = num
    
    return cur_num
    
print(find_mode([0, 1, 1, 2, 1, 2, 0, 1, 1, 0]))