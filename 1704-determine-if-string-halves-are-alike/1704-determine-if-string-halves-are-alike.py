class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set("aeiouAEIOU")
        cnt, half = 0, len(s) // 2  # Use integer division for half to ensure it's an integer

        for i, c in enumerate(s):
            if c in vowels:
                cnt += 1 if i < half else -1 

        return cnt == 0
