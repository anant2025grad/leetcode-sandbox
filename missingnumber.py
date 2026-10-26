#268 Missing Number

# this solution is n(log n) because sorting in python
# is n(log n)

'''

def missingNumber(self, nums):
    nums.sort()

    for i,v in enumerate(nums)
        if(i != v):
            return v-1
        
        if v == len(nums)-1:
            return v+1
            

'''
# better solution
# take two values, the expected sum of list
# and subtract the actual sum of list


def missingNumber(self, nums: List[int]) -> int:
    n = len(nums)
    
    expectedSum = n * (n+1) // 2
    realSum = sum(nums)
    
    return expectedSum - realSum