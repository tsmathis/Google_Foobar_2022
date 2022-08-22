# Question 1 - Prepare the Bunnies' Escape

import copy
from collections import OrderedDict

def solution(maze):
    def check_passable(maze):
        passable = []
        for i in range(len(maze)):
            for j in range(len(maze[i])):
                if maze[i][j] == 1:
                    if (i - 1 >= 0 and i + 1 <= len(maze) - 1) and (maze[i + 1][j] == 0 and maze[i - 1][j] == 0):
                        passable.append((i, j))
                    elif (j - 1 >= 0 and j + 1 <= len(maze[i]) - 1) and (maze[i][j + 1] == 0 and maze[i][j - 1] == 0):
                        passable.append((i, j))

        return passable

    def create_graph(maze):
        vertices = OrderedDict()
        for i in range(len(maze)):
            for j in range(len(maze[i])):
                if maze[i][j] == 1:
                    vertices[(i, j)] = 1
                else:
                    vertices[(i, j)] = 0

        passable = check_passable(maze)

        return vertices, passable[::-1]


    def dijkstra(graph):
        visited = OrderedDict()
        unvisited = OrderedDict((vertex, float("inf")) for vertex, value in graph.items() if value == 0)
        unvisited[list(unvisited.keys())[-1]] = 1

        while unvisited:
            current = min(unvisited, key=unvisited.get)
            x = current[0]
            y = current[1]
            visited[current] = unvisited[current]
            if current == (0, 0):
                break
            for direction in "NESW":
                if direction == "N":
                    child = (x - 1, y)
                elif direction == "E":
                    child = (x, y + 1)
                elif direction == "S":
                    child = (x + 1, y)
                elif direction == "W":
                    child = (x, y - 1)

                if child in visited:
                    continue

                if child in unvisited:
                    tentativeDistance = unvisited[current] + 1
                    if tentativeDistance < unvisited[child]:
                        unvisited[child] = tentativeDistance

            unvisited.pop(current)

        return visited[0, 0]

    vertices, passable = create_graph(maze)
    paths = []
    for i in passable:
        new_maze = copy.deepcopy(vertices)
        new_maze[i] = 0
        d = dijkstra(new_maze)
        paths.append(d)

    return min(paths)


# Question 2 - Find the Access Codes

def count_triplets(l):
    c = [0] * len(l)
    triplet_count = 0
    for i in range(0,len(l)):
        for j in range(0, i):
            if l[i] % l[j] == 0:
                c[i] = c[i] + 1
                triplet_count = triplet_count + c[j]
    return triplet_count


# Question 3 - Fuel Injection Perfection

def fuel_injection(num: str):
    pellets = int(num)
    steps = 0
    while pellets > 1:
        if pellets % 2 == 0:             
            pellets = pellets // 2
        elif pellets == 3 or pellets % 4 == 1: 
            pellets = pellets - 1
        else:                      
            pellets = pellets + 1
        steps += 1
    return steps
