class Solution:
    def exist(self, board, word):
        # 1. Define dimensions
        ROWS = len(board)
        COLS = len(board[0])
        
        # 2. Pre-check: Character Frequency
        grid_counts = {}
        for r in range(ROWS):
            for c in range(COLS):
                char = board[r][c]
                grid_counts[char] = grid_counts.get(char, 0) + 1

        word_counts = {}
        for char in word:
            word_counts[char] = word_counts.get(char, 0) + 1

        for char in word_counts:
            if grid_counts.get(char, 0) < word_counts[char]:
                return False
        
        # 3. Optimization: Start from the rarer end of the word
        if grid_counts.get(word[-1], 0) < grid_counts.get(word[0], 0):
            word = word[::-1]

        def dfs(r, c, i):
            if i == len(word):
                return True # Capital T
                
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or 
                board[r][c] != word[i]):
                return False # Capital F
            
            # Backtracking steps
            temp = board[r][c]
            board[r][c] = '#'
            
            found = (dfs(r + 1, c, i + 1) or 
                     dfs(r, c + 1, i + 1) or 
                     dfs(r - 1, c, i + 1) or 
                     dfs(r, c - 1, i + 1))
            
            board[r][c] = temp
            return found
            
        # 4. Main Search Loop
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        
        return False