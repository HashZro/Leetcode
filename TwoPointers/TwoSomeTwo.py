# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.


### Solution
# Traverse the list with left and right pointers
# Add the two of them and check the result
# If the result is less then the target it mean we need to move the left pointer up, to increase the total sum
# If the result is more, we need to move the right pointer down, to decrease the total sum

class Solution:
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1


        while left < right:
            currSum = numbers[left] + numbers[right]

            if currSum < target:
                left += 1
            elif currSum > target:
                right -= 1
            else:
                return [left + 1, right + 1]
                
            
        return [left + 1, right + 1]

        
        
solution = Solution()

print(solution.twoSum([-1,0], -1))