class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        n = len(graph)
        # 1 << i represent we have visited node i
        # e.g. if i is 1 which mean we have visited node 1. the bitmask should become "10" . 
        queue = list((1 << i, i, 0) for i in range(n))
        visited = list((i << i, i) for i in range(n))
        
        while queue:
            mask, node, dist = queue.pop(0)
            # base case 
            if mask == (1 << n) - 1: 
                return dist

            for child in graph[node]:
                # original mask 100, node 1
                # new_mask -> 101 
                new_mask = mask | ( 1 << child )
                if (new_mask, child) not in visited:
                    visited.append((new_mask, child))
                    queue.append((new_mask, child, dist + 1))


        

if __name__ == '__main__':
    solution = Solution()
    graph = [[1,2,3,4,5,6,7,8,9],[0,2,3,4,5,6,7,8,9],[0,1,3,4,5,6,7,8,9],[0,1,2,4,5,6,7,8,9],[0,1,2,3,5,6,7,8,9],[0,1,2,3,4,6,7,8,9],[0,1,2,3,4,5,7,8,9],[0,1,2,3,4,5,6,8,9],[0,1,2,3,4,5,6,7,9,10],[0,1,2,3,4,5,6,7,8,11],[8],[9]]
    res = solution.shortestPathLength(graph)
    print(res)