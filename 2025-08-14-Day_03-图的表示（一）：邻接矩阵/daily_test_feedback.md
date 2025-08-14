# Day 3: Daily Test & Evaluation

## Question 1

**Question:** Draw (or describe) the undirected graph represented by the following adjacency matrix. The vertices are 0, 1, 2, 3.
```
[[0, 1, 0, 1],
 [1, 0, 1, 0],
 [0, 1, 0, 1],
 [1, 0, 1, 0]]
```

**Student's Answer:** The user provided an image (`a1.png`) showing a graph with 4 vertices connected in a cycle (0-1-2-3-0).

**Evaluation:** `Correct`. The drawing accurately represents the connections in the matrix.

---

## Question 2

**Question:** A social network has four users: Alice, Bob, Carol, and Dave.
- Alice is friends with Bob and Dave.
- Bob is friends with Alice and Carol.
- Carol is friends with Bob and Dave.
- Dave is friends with Alice and Carol.
Create the adjacency matrix for this network (Alice=0, Bob=1, Carol=2, Dave=3).

**Student's Answer:**
```
[[0,1,0,1],
[1,0,1,0],
[0,1,0,1],
[1,0,1,0]]
```

**Evaluation:** `Correct`. The matrix correctly represents the mutual friendships.

---

## Question 3 (Programming)

**Question:** Write a Python function `create_adjacency_matrix(edges, num_vertices)` that takes a list of directed edges and returns the adjacency matrix.

**Student's Code:**
```python
def create_adjacency_matrix(edges, num_vertices):
    matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]
    print(matrix)
    for i in range(num_vertices):
        m,n = edges[i]
        matrix[m][n] = 1
    return matrix
```

**Evaluation:** `Partially Correct`. The code correctly initializes the matrix but contains a bug in the loop `for i in range(num_vertices):`. This assumes the number of edges equals the number of vertices, which is not always true. The correct approach is to iterate directly over the `edges` list.

**Corrected Code:**
```python
def create_adjacency_matrix_corrected(edges, num_vertices):
    matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]
    
    for u, v in edges:
        if u < num_vertices and v < num_vertices:
            matrix[u][v] = 1
            
    return matrix
```
