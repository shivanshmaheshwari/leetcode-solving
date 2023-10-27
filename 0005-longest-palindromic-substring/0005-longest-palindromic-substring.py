class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        # Preprocess the string with special characters
        # to handle even-length palindromes
        processed = self.preprocess(s)

        # Array to store the lengths of palindromes
        palindrome_lengths = [0] * len(processed)
        center = right = 0
        max_length = center_index = 0

        for i in range(1, len(processed) - 1):
            if i < right:
                mirror = 2 * center - i
                palindrome_lengths[i] = min(right - i, palindrome_lengths[mirror])

            while processed[i + 1 + palindrome_lengths[i]] == processed[i - 1 - palindrome_lengths[i]]:
                palindrome_lengths[i] += 1

            if i + palindrome_lengths[i] > right:
                center = i
                right = i + palindrome_lengths[i]

            if palindrome_lengths[i] > max_length:
                max_length = palindrome_lengths[i]
                center_index = i

        start = (center_index - max_length) // 2
        end = start + max_length
        return s[start:end]

    def preprocess(self, s: str) -> str:
        processed = '#'.join('^{}$'.format(s))
        return processed
