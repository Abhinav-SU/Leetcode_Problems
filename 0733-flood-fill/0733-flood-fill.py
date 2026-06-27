class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m,n = len(image),len(image[0])

        if image[sr][sc] == color:
            return image

        dire = [(0,1),(0,-1),(1,0),(-1,0)]
        stack = [(sr,sc)]
        orgColor = image[sr][sc]
        image[sr][sc] = color

        while stack:
            r,c = stack.pop()
            for dr,dc in dire:
                nr,nc = r+dr,c+dc
                if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == orgColor:
                    image[nr][nc] = color
                    stack.append((nr,nc))
        return image

