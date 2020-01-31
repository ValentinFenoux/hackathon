def mat_decouverte(map, i, j):
    mat_dec = numpy.zeros((len(map), len(map[0])), 2), dtype=bool)
    while map[i - 1][j] != "-":
        i -= 1
    while map[i][j - 1] != "-":
        j -= 1
    i0, j0 = i, j
    while map[i][j + 1] != "-":
        j += 1
    j1 = j
    while map[i + 1][j] != "-":
        i += 1
    i1 = i
    for i in range(i0-1, i1 + 2):
        for j in range(j0-1, j1 + 2):
            mat_dec[i][j] = True