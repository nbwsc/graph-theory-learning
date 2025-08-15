graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": []
}


def matrix_to_list(adj_matrix):
    graph = {}
    for i in range(len(adj_matrix)):
        graph[i] = []
        for j in range(len(adj_matrix[i])):
            if adj_matrix[i][j] == 1:
                graph[i].append(j)
    return graph


print(matrix_to_list(graph))
