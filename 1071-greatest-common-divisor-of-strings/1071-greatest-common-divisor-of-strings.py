class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
     
        if str1 + str2 != str2 + str1:
            return ""

        max_length = min(len(str1), len(str2))  
        
        for l in range(max_length, 0, -1):
            if len(str1) % l == 0 and len(str2) % l == 0:
                if str1[:l] * (len(str1) // l) == str1 and str2[:l] * (len(str2) // l) == str2:
                    return str1[:l]  
        
        return "" 