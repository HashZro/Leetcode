# Given 2 strings, return true if they are an anagram of each other and false otherswise

# Sorted both
# Traversed the first one and check if char at "i" was the same in the second one

class Solution:
    def isAnagram(self, s, t) -> bool:
        return sorted(s) == sorted(t)
    
solution = Solution()

solution.isAnagram("anagram", "nagaram")
solution.isAnagram("rat", "car")

print("end")
