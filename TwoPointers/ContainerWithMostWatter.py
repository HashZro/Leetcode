# need to find the greatest area possible

# Not optimal solution:
# Traverse the array from the first and combine it to every item up to the last one, save the largest value in a hashmap at index 1
# Do it again starting from second
# Check the hashmap for the biggest value


class Solution(object):
    def maxArea(self, height):
        biggestValPerIndex = {}

        left = 0
        biggestVal = 0

        while left < len(height) -1:
            right = left + 1

            while right < len(height):
                heightVal = min(height[left], height[right])
                baseVal = right - left

                if heightVal * baseVal  > biggestValPerIndex.get(left, 0):
                    biggestValPerIndex[left] = heightVal * baseVal
                right +=1
            left += 1
        

        for val in biggestValPerIndex:
            if biggestValPerIndex[val] > biggestVal:
                biggestVal = biggestValPerIndex[val]
            
        return print(biggestVal) 
        

        
        
        
solution = Solution()
solution.maxArea([1,8,6,2,5,4,8,3,7])
solution.maxArea([1, 8])
