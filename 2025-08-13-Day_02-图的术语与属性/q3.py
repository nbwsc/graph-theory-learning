def getGraphDegree(graph, N, k):
    degIn = 0
    degOut = 0
    for i in range(N):
        if graph[i][k] == 1:
            degIn += 1
        if graph[k][i] == 1:
            degOut += 1
