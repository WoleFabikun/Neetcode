class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()

        def dfs(row, col):
            if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
                return False

            if grid[row][col] == '0':
                return False

            if (row, col) in seen:
                return False

            seen.add((row, col))

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

            return True

        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if dfs(row, col):
                    islands += 1

        return islands

