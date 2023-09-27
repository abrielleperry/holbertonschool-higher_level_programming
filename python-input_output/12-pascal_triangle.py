#!/usr/bin/python
"""that returns a list of lists of integers
representing the Pascal’s triangle of n"""


def pascal_triangle(n):
    if n <= 0:
        return []
    tri = []
    for i in range(n):
        element_row = [1]
        if 1 > 0:
            prev = tri[i - 1]
            for e in range(1, i):
                    row.append[1]
            tri.append(row)
        return tri
