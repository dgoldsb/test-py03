from test_pyo3 import dijkstra


# Define a graph, nodes would normally be the `id(node)` for some node-class.
start = 1
goal = 7
successors = {
    1: [(1, 5), (1, 2)],
    2: [(1, 3), (1, 6)],
    3: [(1, 4)],
    4: [(1, 7)],
    6: [(10, 7)],
}
path = dijkstra(start, goal, successors)
assert path == [1, 2, 3, 4, 7]
