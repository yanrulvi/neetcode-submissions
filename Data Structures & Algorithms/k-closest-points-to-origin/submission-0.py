class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for i, point in enumerate(points):
            d = point[0] ** 2 + point[1] ** 2
            heapq.heappush(distances, [d, point])
        
        return [heapq.heappop(distances)[1] for _ in range(k)]