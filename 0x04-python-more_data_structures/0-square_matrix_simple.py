def square_matrix_simple(matrix=[]):
    res = []
    for row in matrix:
        auxillary_array = []
        for element in row:
            auxillary_array.append(element * element)
        res.append(auxillary_array)
    return res

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(square_matrix_simple(matrix))

    
