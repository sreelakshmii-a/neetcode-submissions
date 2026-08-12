class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=defaultdict(set)
        col=defaultdict(set)
        box=defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[0])):
                current = board[i][j]
                if current == ".":
                    continue
                elif current in row[i] or current in col[j] or current in box[(i//3,j//3)]:
                    return False
                else:
                    row[i].add(current)
                    col[j].add(current)
                    box[(i//3,j//3)].add(current)
        return True