class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k=len(s1)
        if k>len(s2):
            return False

        dict2={}
        
        for i in range(k):
            dict2[s1[i]]=dict2.get(s1[i],0)+1
        
        window={}
        for r in range(len(s2)):
            window[s2[r]]=window.get(s2[r],0)+1

            if r>=k:
                left_char=s2[r-k]
                window[left_char]-=1
                if window[left_char]==0:
                    del window[left_char]

            if window==dict2:
                return True
        return False
        
