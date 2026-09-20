class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {

        }
        for str in strs:
            signature = tuple(sorted(str))
            
            if signature not in groups:
                groups[signature] = []
            groups[signature].append(str)

        return list(groups.values())