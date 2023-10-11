def square_matrix_simple(matrix=[]):
    
    return list(map(lambda arr: list(map(lambda x: x*x, arr)), matrix))

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(square_matrix_simple(matrix))

    
