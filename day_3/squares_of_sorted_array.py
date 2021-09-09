def sortedSquares(self, nums):
    squared=[]
    for num in nums:
        square = abs(num)**2
        squared.append(square)
    squared.sort()
    return squared
    
        