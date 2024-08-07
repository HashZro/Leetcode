# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


# Solution
# Traverse the array and sort each item
# Sort the array
# traverse the sorted array and push values to a temporary array
# keep pushing as long as the the current value is the same as the last one in the temp array
# when that no longer the case, push the temp array to the response array, and clear the temp array
# do thi until the last item in the array and return the response array

# OBS: shouldnt modify the strings
# skip the sort part and only sort to compare, but same it unmodified


class Solution(object):
    def groupAnagrams(self, strs):
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
            
            res[tuple(count)].append(s)

        return res.values()
            





        responseArray.append(strs[len(strs) -1])
        strs.pop()

        curIndex = 0
        curPointer = len(strs)

        while len(strs) != 0:
            if sorted(responseArray[curIndex][0]) == sorted(strs[curPointer]):
                responseArray[curIndex].append(strs[curPointer])
                curPointer -= 1
                strs.pop()
            else:
                responseArray[curIndex].append(strs[curPointer])
                curIndex += 1
                curPointer -= 1
                strs.pop()
            
        return print(responseArray)        

solution = Solution()
solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])