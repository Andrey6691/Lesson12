def get_matrix (n, m, value):
    matrix=[]
    for i in range(n):
        matrix.append([])
        for j in range(m):
                matrix[i].append(value)
    return matrix

print(get_matrix(5, 5, 10))
print(get_matrix(7, 7, 16))
print(get_matrix(10, 3, 100))
