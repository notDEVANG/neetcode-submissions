class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        current_window = set()
        max_length = 0

        for r in range(len(s)):
            while s[r] in current_window:
                current_window.remove(s[l])
                l += 1
            current_window.add(s[r])
            max_length = max(max_length, r - l + 1)
        return max_length