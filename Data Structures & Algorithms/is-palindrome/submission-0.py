class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left=0
        check="".join(char.lower() for char in s if char.isalnum())
        right=len(check)-1
        while left<=right:
            if check[left]!=check[right]:
                return False
            left+=1
            right-=1
        return True
