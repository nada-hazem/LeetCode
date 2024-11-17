class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        vowels = {"a", "e", "i", "o", "u"}
        cur_vow = sum(1 for char in s[:k] if char in vowels)
        max_vow = cur_vow

        for i in range(k, n):
            if s[i - k] in vowels:
                cur_vow -= 1
            if s[i] in vowels:
                cur_vow += 1
            max_vow = max(max_vow, cur_vow)

        return max_vow
