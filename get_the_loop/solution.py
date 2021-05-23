# https://www.codewars.com/kata/52a89c2ea8ddc5547a000863/train/python
def loop_size(node):
    visited = {}
    ply = 0
    n = node
    while True:
        if n in visited:
            return ply - visited[n]
        visited[n] = ply
        ply += 1
        n = n.next


class Node:
    pass
