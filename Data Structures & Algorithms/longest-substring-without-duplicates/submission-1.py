class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left = 0
        right = 0
        d = defaultdict(int)
        
        while right < len(s):
            if s[right] in d and d[s[right]] > 0:
                res = max(res, right - left)
                while d[s[right]] > 0:
                    d[s[left]] -= 1
                    left += 1
            d[s[right]] += 1
            right += 1
        
        return max(res, right - left)