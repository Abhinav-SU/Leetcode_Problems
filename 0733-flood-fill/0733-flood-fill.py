class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orColor = image[sr][sc]
        if orColor == color:
            return image
        dire = [(0,1),(0,-1),(1,0),(-1,0)]
        stack =[(sr,sc)]
        image[sr][sc] =color

        while stack:
            r,c = stack.pop()
            for dr,dc in dire:
                nr,nc = r+dr,c+dc
                if 0 <= nr <len(image) and 0 <= nc < len(image[0]) and image[nr][nc]==orColor:
                    image[nr][nc]=color
                    stack.append((nr,nc))
        return image

