class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uni=set()
        l=0
        r=l+1
        if not s:
            return 0
        uni.add(s[l])
        max_len=1
        while r<len(s):
            if s[r] in uni:
                while s[r] in uni:
                    uni.remove(s[l])
                    l+=1
                uni.add(s[r])
                    
            else:
                uni.add(s[r])
                max_len=max(max_len,len(uni))
            r+=1
        return max_len

