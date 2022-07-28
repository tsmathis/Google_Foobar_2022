# Question 1

import itertools

def coded_message(L):

    res = []

    for r in range(1, len(L)+1):
        res.append([''.join(str(i) for i in j) for j in itertools.permutations(L, r)])

    res = sorted(list(int(i) for i in itertools.chain.from_iterable(res)), reverse=True)

    for i in res:
        if i % 3 == 0:
            return i
    
    return 0

# Question 2
from collections import deque

def chess_board_BFS(src, dest):

    if src == dest:
        return 0

    def valid_move(move, x_pos, y_pos):
        if move == "1":
            x_pos -= 2
            y_pos += 1
        elif move == "2":
            x_pos -= 1
            y_pos += 2
        elif move == "3":
            x_pos += 1
            y_pos += 2
        elif move == "4":
            x_pos += 2
            y_pos += 1
        elif move == "5":
            x_pos += 2
            y_pos -= 1
        elif move == "6":
            x_pos += 1
            y_pos -= 2
        elif move == "7":
            x_pos -= 1
            y_pos -= 2
        elif move == "8":
            x_pos -= 2
            y_pos -= 1

        if not (0 <= x_pos <= 7 and 0 <= y_pos <= 7):
            return False
            
        return True

    def next_position(move, x_pos, y_pos):
        if move == "1":
            x_pos -= 2
            y_pos += 1
        elif move == "2":
            x_pos -= 1
            y_pos += 2
        elif move == "3":
            x_pos += 1
            y_pos += 2
        elif move == "4":
            x_pos += 2
            y_pos += 1
        elif move == "5":
            x_pos += 2
            y_pos -= 1
        elif move == "6":
            x_pos += 1
            y_pos -= 2
        elif move == "7":
            x_pos -= 1
            y_pos -= 2
        elif move == "8":
            x_pos -= 2
            y_pos -= 1

        return x_pos, y_pos

    if src < 8:
        start_x = 0
        start_y = src
    else:
        start_x = src // 8
        start_y = src - 8 * start_x

    if dest < 8:
        goal_x = 0
        goal_y = dest
    else:
        goal_x = dest // 8
        goal_y = dest - 8 * goal_x

    visited = {}
    queue = deque()
    moves = ["1", "2", "3", "4", "5", "6", "7", "8"]

    queue.append((start_x, start_y))
    visited[(start_x, start_y)] = None
    cont = True

    while cont:
        x, y = queue.popleft()
        valid_moves_new_position = 0
        for move in moves:
            if valid_move(move, x, y):
                valid_moves_new_position += 1
                next_x, next_y = next_position(move, x, y)
                
                if (next_x == goal_x and next_y == goal_y):
                    visited[(next_x, next_y)] = (x, y)
                    cont = False
                    break

                if (next_x, next_y) not in visited:
                    visited[(next_x, next_y)] = (x, y)
                    queue.append((next_x, next_y))

    steps = 0
    key = (next_x, next_y)
    while visited[key] != None:
        key = visited[key]
        steps += 1
    
    return steps
    