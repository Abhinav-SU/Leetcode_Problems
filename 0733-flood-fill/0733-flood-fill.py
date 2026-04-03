from collections import deque


class Solution:
    def floodFill(self, image, sr, sc, color):
        originalColor = image[sr][sc]
        if originalColor == color:
            return image

        n, m = len(image), len(image[0])

        q = deque()

        q.append((sr, sc))
        image[sr][sc] = color

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m:
                    if image[nr][nc] == originalColor:
                        image[nr][nc] = color
                        q.append((nr, nc))

        return image
