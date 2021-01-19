import math
import sys

class Node:

    def __init__(self, state: tuple) -> None:
        self.state = state
        self.pos = self.find_pos()


    def to_list(self):
        return [[self.state[0],self.state[1], self.state[2]], [self.state[3], self.state[4], self.state[5]], [self.state[6], self.state[7], self.state[8]]]

    def swap(self, _from, _to):
        temp = self.to_list()
        temp[_from[0]][_from[1]], temp[_to[0]][_to[1]] = temp[_to[0]][_to[1]], temp[_from[0]][_from[1]]
        return Node((*temp[0], *temp[1], *temp[2]))


    def get_new_nodes(self):
        nodes = []
        if self.pos[1] != 2:
            nodes.append(self.swap(self.pos, (self.pos[0], self.pos[1] + 1)))
        if self.pos[1] != 0:
            nodes.append(self.swap(self.pos, (self.pos[0], self.pos[1] - 1)))
        if self.pos[0] != 2:
            nodes.append(self.swap(self.pos, (self.pos[0] + 1, self.pos[1])))
        if self.pos[0] != 0:
            nodes.append(self.swap(self.pos, (self.pos[0] - 1, self.pos[1])))
        return nodes

    def __repr__(self) -> str:
        return '\n'.join(map(str, self.to_list()))

    def find_pos(self):
        l = self.to_list()
        for i in range(3):
            for j in range(3):
                if l[i][j] == '*':
                    return i, j

    def __hash__(self) -> int:
        return hash(self.state)


    def __eq__(self, o: object) -> bool:
        return self.state.__eq__(o.state)


graph = dict()
node = Node((1, 2, 3, '*', 4, 6, 7, 5, 8))
print(sys.getsizeof(node))
queue = [node]

while len(queue) > 0:
    cur_node = queue.pop()
    new_nodes = cur_node.get_new_nodes()
    graph[cur_node] = new_nodes
    for _node in new_nodes:
        if _node not in graph:
            queue.append(_node)
print(sys.getsizeof(graph))

# distances = {_node: math.inf for _node in graph.keys()}
# distances[node] = 0
# visited = set()
#
# while len(visited) < len(distances):
#     _next = min(list(filter(lambda x: x[0] not in visited, distances.items())), key=lambda x: x[1])
#     neighbors = graph[_next]
#     for i in neighbors:
#         if distances[_next] + 1 < distances[i]:
#             distances[i] = distances[_next] + 1
#     visited.add(_next)


# 2, 3, 4
# 1, 5, '*'
# 7, 6, 8
#
