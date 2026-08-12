class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hash_ = defaultdict(list)

        for i in range(9):
            for j in range(9):
                el = board[i][j]
                if el.isdigit():
                    hash_[f"r{i}"].append(el)
                    hash_[f"c{j}"].append(el)
                    hash_[f"s{i // 3}{j // 3}"].append(el)

        for key in hash_.keys():
            if len(hash_[key]) != len(set(hash_[key])):
                return False
        return True
