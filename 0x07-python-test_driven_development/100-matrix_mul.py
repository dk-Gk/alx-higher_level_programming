#!/usr/bin/python3
"""matrix multiplication"""

def matrix_mul(m_a, m_b):
    """matrix multiplication"""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    elif not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    elif not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    elif not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    elif m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    elif m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    elif not all((isinstance(ele, int) or isinstance(ele, float))
                 for ele in [x for row in m_a for x in row]):
        raise TypeError("m_a should contain only integers or floats")
    elif not all((isinstance(ele, int) or isinstance(ele, float))
                 for ele in [x for row in m_b for x in row]):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    
    i_b = []
    for i in range(len(m_b[0])):
        new = []
        for j in range(len(m_b)):
            new.append(m_b[j][i])
        i_b.append(new)

    new_matrix = []
    for j in m_a:
        new = []
        for k in i_b:
            res = 0
            for z in range(len(i_b[0])):
                res += j[z] * k[z]
            new.append(res)
        new_matrix.append(new)
    
    return new_matrix
