class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels =set("aeiouAEIOU")
        slist = list(s)
        
        i=0 
        j= len(s)-1
        
        while i < j :
            if slist[i] not in vowels :
                i+=1
            elif slist[j] not in vowels:
                j-=1
        
            else :
                slist[i],slist[j] = slist[j],slist[i]
                
                i+=1
                j-=1
               
        
        return "".join(slist)
          