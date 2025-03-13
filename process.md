BFS 
queue (first in first out)

[0, 1, 2, 3]

0 -> 1 -> 0 -> 1  (infinity loop) 
0 -> 1 -> 0 -> 2 -> 0 -> 3
0 -> 1 -> 0 -> 3 -> 0 -> 2

# bitmask with current node
1111




n is the among of nodes
# base case
(1 << n) - 1


# create queue 
starting from 0 
(1, 0, 0)

starting from 1
(2, 1, 0)

starting from 2
(4, 2, 0)

starting from 3
(8, 3, 0)


# example (starting from node 0)
example: 0 -> 1 -> 0 -> 2 -> 0 -> 3

from node 0 to node 1 / current node 1 / 0
1. 11

from node 1 to node 0 / current node 0 / 1
2. 11

from node 0 to node 2 / current node 2 / 2
3. 111

from node 2 to node 0 / current node 0 / 3
4. 111

from node 0 to node 3 / current node 3 / 4
5. 1111
