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

    for i in range(n):
        row = [1]
        if i > 0:
            prev = triangle[i - 1]
            for j in range(1, i):
                row.append(prev[j - 1] + prev[j])
            row.append(1)
        triangle.append(row)

    return triangle
