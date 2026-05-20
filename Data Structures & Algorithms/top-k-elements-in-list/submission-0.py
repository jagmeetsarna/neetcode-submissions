class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dic={}
        for i in nums:
            if dic.get(i):
                dic[i]=dic[i]+1
            else:
                dic[i]=1
        
        sorted_dic = sorted(dic.items(),key=lambda kv:kv[1], reverse=True)

        sorted_dic = [i[0] for i in sorted_dic[:k]]

        return sorted_dic