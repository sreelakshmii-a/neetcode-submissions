class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={s[0]:1}
        l=0
        r=1
        max_len=1
        while r<len(s):
            win_len=r-l+1
            count[s[r]]=count.get(s[r],0)+1

            max_freq=max(count.values())
            replaceable=win_len-max_freq
            if replaceable>k:
                count[s[l]] = count.get(s[l]) - 1
                l+=1
            else:
                max_len=max(max_len,win_len)

            r+=1
        return max_len

                

            