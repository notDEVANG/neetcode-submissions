class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = Counter()
        left = 0
        max_length = 0

        for right in range(len(s)):
            count[s[right]] += 1                        # add new char to window

            window_size = right - left + 1
            max_freq = max(count.values())

            if window_size - max_freq > k:              # window invalid → shrink one step
                count[s[left]] -= 1
                left += 1

        # after any shrink, window is valid → record its size
            max_length = max(max_length, right - left + 1)

        return max_length