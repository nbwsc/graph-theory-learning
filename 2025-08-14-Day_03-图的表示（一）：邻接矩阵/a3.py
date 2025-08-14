def create_adjacency_matrix(edges, num_vertices):
    matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]
    print(matrix)
    for i in range(num_vertices):
        m,n = edges[i]
        matrix[m][n] = 1
    return matrix

print(create_adjacency_matrix([(0,1), (0,2), (1,2), (1,3)], 4))