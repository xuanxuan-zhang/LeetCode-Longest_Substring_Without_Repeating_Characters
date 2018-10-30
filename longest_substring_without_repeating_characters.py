class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) > 0:
            substring = s[0]
            Length = 1
        else:
            return 0
        for i in range(1, len(s)):
            if s[i] not in substring:
                substring = substring + s[i]
            else:
                Length = max(len(substring), Length)
                ind = substring.find(s[i])
                substring = substring[ind+1:len(substring)] + s[i]

        Length = max(len(substring), Length)
        return Length


test = Solution()
output = test.lengthOfLongestSubstring('abcabcbb')
print('The length of the longest substring is {}'.format(output))
