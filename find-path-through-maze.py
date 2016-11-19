#!/usr/bin/env python3

from copy import copy

def bfs_find_path_through_maze(maze, start, finish):
    seen = set()
    def point_from(point, direction):
        dimy = len(maze)
        dimx = len(maze[0])
        r, c = point
        if direction == 'n': r -= 1
        if direction == 'e': c += 1
        if direction == 's': r += 1
        if direction == 'w': c -= 1
        if 0 <= r < dimy and 0 <= c < dimx:
            if (r, c) in seen:
                return
            if (r, c) == start:
                return
            if maze[r][c] != 0:
                return
            seen.add((r, c))
            return r, c

    queue = [(start, [start])]
    while queue:
        point, path = queue[0]
        queue = queue[1:]
        for direction in 'n', 'e', 's', 'w':
            npoint = point_from(point, direction)
            if not npoint:
                continue
            path.append(npoint)
            if npoint == finish:
                return path
            else:
                queue.append((npoint, copy(path)))

def dfs_find_path_through_maze(maze, start, finish):
    dimy = len(maze)
    dimx = len(maze[0])
    seen = set()
    def dfs(point, path):
        seen.add(point)
        r, c = point
        if (r, c) == finish:
            return True
        for r, c in ( (r-1,c), (r,c+1), (r+1,c), (r,c-1) ):
            if (r, c) in seen:
                continue
            if not (0 <= r < dimy and 0 <= c < dimx):
                continue
            if (r, c) == start:
                continue
            if maze[r][c] != 0:
                continue
            path.append((r, c))
            if dfs((r, c), path):
                return True
            path.pop()
        return False
    path = [start]
    dfs(start, path)
    return path

maze = [
    [0, 0, 1, 1, 1, 0],
    [1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 1, 0],
]

x = dfs_find_path_through_maze(maze, (0,0), (5,5))
print(x)
