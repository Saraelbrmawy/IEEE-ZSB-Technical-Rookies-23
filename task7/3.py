class Solution:
    def kClosestpoint(self, points, K):
        def dis(point):
            return ((point[0] - 0)**2 + (point[1] - 0)**2)**0.5
        return sorted(points, key=dis)[:K]