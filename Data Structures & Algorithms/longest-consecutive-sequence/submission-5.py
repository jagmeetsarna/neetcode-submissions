class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        longest_streak = 0
        nums_=[]
        for i in nums:
            if i -1  not in nums:
                current_num = i
                current_streak = 1

                while current_num+1 in nums:
                    current_num+=1
                    current_streak+=1
                longest_streak = max(longest_streak,current_streak)

        return longest_streak