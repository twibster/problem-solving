def majorityElement(nums):
    count =0
    maj = len(nums)//2
    tested=[]
    for num in nums:
        if num not in tested:
            tested.append(num)
            now = nums.count(num)
            if now > maj:
                count =now
                hero = num
    return hero