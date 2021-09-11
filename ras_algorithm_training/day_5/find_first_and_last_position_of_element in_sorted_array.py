def Binary(nums, target):
    low= 0
    high = len(nums)- 1
    while low<=high and len(nums) != 0:
        mid = (high + low)//2
        if target == nums[mid]:
            return mid
        elif target <nums[mid]:
            high = mid -1
        else:
            low = mid +1
            
def searchRange(nums,target):
    limit=[]
    result =Binary(nums,target)

    if result == None:
        return [-1,-1]

    while result != None:
        nums.pop(result)
        while result in limit:
            result += 1
        else:
            limit.append(result)
        result = Binary(nums,target)

    if len(limit) ==1:
        limit.append(limit[0])

    limit.sort()
    
    return [limit[0],limit[-1]]
