# Day 02: 图的术语与属性 (Graph Terminology and Properties)

## 1. 顶点的度 (Degree of a Vertex)

“度”是描述一个顶点连接了多少条边的概念。

- **无向图 (Undirected Graph)**:
  - **度 (Degree)**, `deg(v)`: 与顶点 `v` 相关联的边的数量。

- **有向图 (Directed Graph)**:
  - **出度 (Out-degree)**: 从顶点 `v` 出发的边的数量。
  - **入度 (In-degree)**: 进入顶点 `v` 的边的数量。
  - **基本定理**: 在任何有向图中，所有顶点的入度之和等于所有顶点的出度之和，这个值也等于图的总边数。
    - Σ(in-degree(v)) = Σ(out-degree(v)) = |E|

## 2. 路径 (Path) 与 环 (Cycle)

- **路径 (Path)**:
  - 一个顶点的序列 `(v1, v2, ..., vk)`，其中任意相邻的两个顶点 `(vi, vi+1)` 都有边相连。
  - **路径长度**: 路径上边的数量，即 `k-1`。
  - **简单路径 (Simple Path)**: 路径上所有顶点都是唯一的（起点和终点可能相同）。

- **环 (Cycle / Circuit)**:
  - 一条起点和终点相同的路径。
  - **简单环 (Simple Cycle)**: 环中除了起点和终点相同外，其他所有顶点都是唯一的。
  - 在无向图中，一个简单环至少需要3个顶点。

## 3. 连通性 (Connectivity)

- **无向图**:
  - **连通 (Connected)**: 如果从顶点 `u` 到 `v` 存在一条路径。
  - **连通图 (Connected Graph)**: 图中任意两个顶点都是连通的。
  - **连通分量 (Connected Components)**: 如果图不连通，其内部的极大连通子图。

- **有向图**:
  - **弱连通 (Weakly Connected)**: 将所有有向边替换为无向边后，得到的图是连通的。
  - **强连通 (Strongly Connected)**: 对于图中任意一对顶点 `u` 和 `v`，既存在从 `u` 到 `v` 的路径，也存在从 `v` 到 `u` 的路径。

## 4. 稀疏图 (Sparse Graph) 与 稠密图 (Dense Graph)

这是一个相对概念，用于描述图中边的数量。

- **稀疏图 (Sparse Graph)**:
  - 边的数量 `|E|` 远小于最大可能边的数量。
  - 通常 `|E|` 与 `|V|` 是一个数量级，即 `|E| ≈ O(|V|)`。
  - **存储推荐**: 邻接表 (Adjacency List)。

- **稠密图 (Dense Graph)**:
  - 边的数量 `|E|` 接近最大可能边的数量。
  - 通常 `|E|` 与 `|V|^2` 是一个数量级，即 `|E| ≈ O(|V|^2)`。
  - **存储推荐**: 邻接矩阵 (Adjacency Matrix)。
