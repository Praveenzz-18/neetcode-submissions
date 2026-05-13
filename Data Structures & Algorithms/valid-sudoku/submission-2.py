class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSets = [set() for _ in range(9)]    
        colSets = [set() for _ in range(9)]    
        subGridSets = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(9):
            for c in range(9):
                elem = board[r][c]
                if elem == '.':
                    continue
                
                if elem in rowSets[r]:
                    return False
                
                if elem in colSets[c]:
                    return False

                if elem in subGridSets[r // 3] [c // 3]:
                    return False
                
                rowSets[r].add(elem)
                colSets[c].add(elem)
                subGridSets[r//3][c//3].add(elem)
        
        return True