class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s_stripped = "".join([i.lower() for i in s if i.isalnum()])
        if len(s_stripped) <= 1:
            return True

        counter_left=0
        counter_right = len(s_stripped)-1

        while counter_left<counter_right:
            if s_stripped[counter_left] == s_stripped[counter_right]:
                counter_left+=1
                counter_right-=1
            else:
                return False
        
        return True

        