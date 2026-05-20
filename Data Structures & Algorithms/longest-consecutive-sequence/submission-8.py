class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = list(sorted(set(nums)))

        max_counter = 0
        for j in range(len(sorted_nums)):

            counter=1
            for i in range(len(sorted_nums)-1):

                if sorted_nums[i] == sorted_nums[i+1]-1:
                    counter+=1
                    max_counter = max(counter,max_counter)
                else:
                    counter =1
                    

            max_counter = max(counter,max_counter)

        return max_counter