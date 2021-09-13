def rotate(nums, k,sol = 'fast'):
    
    '''my lovely solution (beats 97%) -- get an array to be rotated.
    
                            A note for me:
    ( k = k -n ) is faster than ( k -= n ) according to leetcode runtime estimation
    '''
    if sol == 'fast':
        n = len(nums)
        while k>len(nums): 
            k = k -n
        nums[:] = nums[-k:] + nums[:-k]

    '''slice by the last element one by one'''
    else:
        for r in range(k):
            last = nums[-1]
            nums.insert(0,last)
            nums.pop(-1)

    return nums