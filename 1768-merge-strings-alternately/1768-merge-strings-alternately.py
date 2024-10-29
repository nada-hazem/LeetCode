class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged=[]
        for i in range (min(len(word1),len(word2))):
         merged.append(word1[i])
         merged.append(word2[i])
        if len(word1) > len(word2):
            merged.append(word1[len(word2):])
        else:
            merged.append(word2[len(word1):])
        return ''.join(merged)

if __name__ == "__main__":
    solution = Solution()
    word1 = "ab"
    word2 = "pqrs"
    result = solution.mergeAlternately(word1 , word2)
    print(result)



        