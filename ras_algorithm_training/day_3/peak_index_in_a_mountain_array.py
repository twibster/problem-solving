def peakIndexInMountainArray(arr):
    count =0
    max= 0
    for elem in arr:
        count += 1
        for rest in arr:
            if elem >= rest and elem >=max:
                index =count
                max =elem
            else:
                break
    return index-1