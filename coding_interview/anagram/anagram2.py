class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = s.replace(" ","").lower()
        t = t.replace(" ","").lower()
        
        if len(s) != len(t):
            return False
        
        count = {}
        
        for val1 in s:
            if val1 in count:
                count[val1] +=1
            else:
                count[val1] =1
        
        for val2 in t:
            if val2 in count:
                count[val2] -=1
            else:
                count[val2] =1
        
        for k in count:
            if count[k] != 0:
                return False
            
        return True 
