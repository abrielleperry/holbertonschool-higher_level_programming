#!/usr/bin/python
"""that returns a list of lists of integers
representing the Pascal’s triangle of n"""


def pascal_triangle(n):
    """
    Returns:returns list w first and last element always being 1
    """
    triangle = []
    if n <= 0:
        return triangle

    for i in range(0, n):
        nxt_row = []
        for j in range(0, i + 1):
            if j == 0 or j == i:
                nxt_row.append(1)
            else:
                nxt_n = triangle[i - 1][j - 1] + triangle[i - 1][j]
                nxt_row.append(nxt_n)
        triangle.append(nxt_row)
    return triangle
