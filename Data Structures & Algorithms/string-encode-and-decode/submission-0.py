class Solution:
    width = 3
    m = 3
    def encode(self, strs: List[str]) -> str:
        sizes = []
        res = []
        for str_ in strs:
            sizes.append(len(str_))
        res.append(f"{len(strs):0{self.m}d}")
        for size in sizes:
            res.append(f"{size:0{self.width}d}")
        for str_ in strs:
            res.append(str_)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        n = int(s[:self.m])
        index = self.m + n * self.width
        for i in range(self.m, self.width * n + 1, self.width):
            size_ = int(s[i:i + self.width])
            line = s[index:index + size_]
            res.append(line)
            index += size_
        return res