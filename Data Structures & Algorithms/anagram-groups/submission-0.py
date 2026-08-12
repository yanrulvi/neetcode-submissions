class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        vectors = []
        null = ord('a')
        for line in strs:
            vector = [0] * 26
            for j in range(len(line)):
                vector[ord(line[j]) - null] += 1
            vector = tuple(vector)
            groups[vector] = groups.get(vector, []) + [line]
        return list(groups.values())

