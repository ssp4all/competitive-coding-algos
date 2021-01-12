https://leetcode.com/problems/k-closest-points-to-origin/solution/
import heapq
def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
    heap = []
    
    for (x, y) in points:
        dist = -(x*x + y*y)
        if len(heap) == K:
            heapq.heappushpop(heap, (dist, x, y))
        else:
            heapq.heappush(heap, (dist, x, y))
    
    return [(x,y) for (dist,x, y) in heap]


JAVA
class Solution {
    public int[][] kClosest(int[][] points, int K) {
        // Arrays.sort(points, (p1, p2) -> (p1[0]*p1[0] + p1[1]*p1[1] - p2[0]*p2[0] - p2[1]*p2[1]));
        // return Arrays.copyOfRange(points, 0, K);
        PriorityQueue<int[]> pq = new PriorityQueue<int[]>((p1, p2) -> p2[0] * p2[0] + p2[1] * p2[1] - p1[0] * p1[0] - p1[1] * p1[1]);
        for (int[] p: points){
            System.out.println(Arrays.toString(p));
            pq.offer(p);
            if (pq.size() > K)
                pq.poll();
        }
        int[][] res = new int[K][2];
        while (K > 0)
            res[--K] = pq.poll();
        
        return res;
    }
}