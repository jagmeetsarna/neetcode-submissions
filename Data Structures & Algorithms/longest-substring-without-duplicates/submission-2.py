class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<1:
            return 0


        ss=[]
        for i in range(len(s)):
            kk=[]
            for j in range(i,len(s)):
                if s[j] not in kk:
                    kk.append(s[j])
                else:
                    ss.append(kk)
                    break
            ss.append(kk)  
        maximaz = max([len(i) for i in ss])

        return maximaz     
        