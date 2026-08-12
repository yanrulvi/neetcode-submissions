class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for line in strs:
            vector = [0] * 26
            for j in range(len(line)):
                vector[ord(line[j]) - ord('a')] += 1
            groups[tuple(vector)].append(line)
        return list(groups.values())

