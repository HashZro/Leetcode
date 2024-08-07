# I remember subtraction is key in this problem
# If I traverse the array and subtract the current value from the target, I'll get the value which combine with the current one will hit the target
# Ex. At index zero there is a number that need to be pared with 5 to hit the target
# In that case we save five pointing to zero
# Whenever we find a five, we check the hashmap and it says index zero
# We then combine zero with the current index and return in the array

# Time O(n) = Traverse only once
# Space O(n) = Can go up to the array size

# I have to save the actual value pointing to the index, not the diff.
# Bacause when I'm checkin using the difference I need to know if theres an index with that value, not an index with that difference

class Solution(object):
    def twoSum(self, nums, target):
        targetSum = {}

        for index, val in enumerate(nums):
            diff = target - val
            
            if diff in targetSum:
                return [targetSum[diff], index]
            
            targetSum[val] = index

        return

solution = Solution()
print(solution.twoSum([2,7,11,15], 9))
print(solution.twoSum([3,2,4], 6))
print(solution.twoSum([3,3], 6)) 

