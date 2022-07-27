from math import sqrt

def solution(area):
    res = []
    while area > 0:
        square = int(sqrt(area))**2
        area -= square
        res.append(square)
    return res
