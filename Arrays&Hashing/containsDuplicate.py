# Traverse array and push values to a hashset
# if any any point the value is already in the hashset, return true
# Return false by default, after ther loop

# Time O(n)
# Space O(n)


class Solution:
    def containsDuplicate(self, nums) -> bool:
        my_set = set()

        for number in nums:
            if number in my_set:
                print("True")
                
                return True
            else:
                my_set.add(number)

        print("False")
        return False
    
test = Solution()

test.containsDuplicate([1,2,3,1])
test.containsDuplicate([1,2,3,4])
test.containsDuplicate([1,1,1,3,3,4,3,2,4,2])

