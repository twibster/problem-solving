def rotate(nums, k,sol = 'fast'):
    
    '''slice the rotated array'''
    if sol == 'fast':
        nums = nums[-k:] + nums[:-k]
        return nums

    '''slice by the last element one by one'''
    else:
        for r in range(k):
            last = nums[-1]
            nums.insert(0,last)
            nums.pop(-1)

    return nums