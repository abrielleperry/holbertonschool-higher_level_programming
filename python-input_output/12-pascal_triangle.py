#!/usr/bin/python
"""that returns a list of lists of integers
representing the Pascal’s triangle of n"""


def pascal_triangle(n):
    """

    Returns:returns list w first and last element always being 1
        
    """
    if n <= 0:
        return []

    tri = []
    for i in range(n):
        row = [1]
        if i > 0:
            prev = tri[i - 1]
            for e in range(1, i):
                row.append(prev[e - 1] + prev[e])
            row.append(1)
        tri.append(row)

    return tri
