class Solution:
    def isValid(self, s: str) -> bool:
        n=len(s)
        operators={'{':'}','[':']','(':')'}
        checklist=[]
        
        for x in s:
            if x in ['[','{','(']:
                checklist.append(x)
            elif x in [']','}',')'] and len(checklist)!=0:
                a=checklist.pop()
                if x!=operators[a]:
                    return False
            elif x in [']','}',')'] and len(checklist)==0:
                return False
        return len(checklist)==0