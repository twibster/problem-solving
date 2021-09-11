def findMedianSortedArrays(nums1, nums2):
    merged = nums1 + nums2
    merged.sort()
    return median(merged)
    
def median(arr): 
    length = len(arr)
    if length%2 ==0:
        median = ((arr[length//2] + arr[(length//2)-1])/2) + 0.5
    else:
        median = arr[length//2]

    return median