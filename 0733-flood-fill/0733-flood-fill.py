class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        dire = [(0,1),(0,-1),(1,0),(-1,0)]
        orCol = image[sr][sc]
        def dfs(sr,sc):
            stack =[(sr,sc)]
            image[sr][sc] = color
            while stack:
                r,c = stack.pop()
                for dr,dc in dire:
                    nr,nc = r+dr,c+dc
                    if 0 <= nr < len(image) and 0 <= nc < len(image[0]) and image[nr][nc]== orCol:
                        image[nr][nc]= color
                        stack.append((nr,nc))

            return image


        return dfs(sr,sc) if image[sr][sc] != color else image

