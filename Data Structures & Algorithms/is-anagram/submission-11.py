class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        if len(s) != len(t):
            return False 
        for c in s:
            if c not in s_dict:
                s_dict[c] = 1 
            else :
                s_dict[c]+= 1
        for d in t:
            if d not in t_dict:
                t_dict[d] = 1
            else:
                t_dict[d] += 1
        
        # if s_dict == t_dict:
        #     return True
        # else:
        #     return False 

        if len(s_dict) != len(t_dict):
            return False
        
        for k,v in s_dict.items():
            if k not in t_dict or v!= t_dict[k]:
                return False
 
        return True 

                