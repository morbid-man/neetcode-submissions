class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        results = defaultdict(list)
        for s in strs:
            hash_table = [0]*26
            for char in s:
                hash_table[ord(char) - ord('a')] += 1
            results[tuple(hash_table)].append(s)
        return list(results.values())