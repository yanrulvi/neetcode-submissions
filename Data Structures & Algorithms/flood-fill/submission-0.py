class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        seen = set()
        def paint(sr, sc, color, old_color):
            nonlocal seen
            nonlocal image
            if image[sr][sc] != old_color:
                return
            image[sr][sc] = color
            seen.add((sr, sc))
            if sr - 1 >= 0 and (sr - 1, sc) not in seen:
                paint(sr - 1, sc, color, old_color)
            if sr + 1 < len(image) and (sr + 1, sc) not in seen:
                paint(sr + 1, sc, color, old_color)
            if sc - 1 >= 0 and (sr, sc - 1) not in seen:
                paint(sr, sc - 1, color, old_color)
            if sc + 1 < len(image[0]) and (sr, sc + 1) not in seen:
                paint(sr, sc + 1, color, old_color)
        
        paint(sr, sc, color, image[sr][sc])
        return image
