#!/usr/bin/python3
""" This module supplies a function pascal triangle """


def pascal_triangle(n):
    """
    Find a list of lists of integers representing the Pascal’s
    triangle of n

    Args:
        n(int): number

    Return:
        returns a list of lists of integers
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    new_list = [1]
    old_list = pascal_triangle(n-1)
    for i in range(1, len(old_list[-1])):
        new_list.append(old_list[-1][i] + old_list[-1][i - 1])
    new_list.append(1)
    old_list.append(new_list)
    return old_list
