import numpy as np

def revelation(map, map_decouverte, coord, di, dj):
    if map[coord[0]][coord[1]] == "#":
        for direction in ([0, 1], [0, -1], [1, 0], [-1, 0]):
                i = coord[0] + direction[0]
                j = coord[1] + direction[1]
                if map[i][j] == "#" or map[i][j] == "+":
                    map_decouverte[i][j] == True
    elif map[coord[0]][coord[1]] == "+":
        indices = np.array(coord) + np.array([di, dj])
        while map[indices[0] - 1][indices[1]] != "-":
            indices[0] -= 1
        while map[indices[0]][indices[1] - 1] != "¦":
            indices[1] -= 1
        i0, j0 = indices[0], indices[1]
        while map[indices[0]][indices[1] + 1] != "¦":
            indices[1] += 1
        j1 = indices[1]
        while map[indices[0] + 1][indices[1]] != "-":
            indices[0] += 1
        i1 = indices[0]
        for i in range(i0-1, i1 + 2):
            for j in range(j0-1, j1 + 2):
                map_decouverte[i][j] == True