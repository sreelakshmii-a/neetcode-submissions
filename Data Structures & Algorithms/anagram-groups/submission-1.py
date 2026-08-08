class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        values=defaultdict(list)
        for string in strs:
            str_val=tuple(sorted(char for char in string))
            values[str_val].append(string)
        
        return list(values.values())

        