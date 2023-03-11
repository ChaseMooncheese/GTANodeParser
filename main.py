import typing
import json
import networkx as nx
import matplotlib.pyplot as plt
import scipy

class Node():
    def __init__(self, x, y, z):
        self.x: float = x
        self.y: float = y
        self.z: float = z

class NodeEdge():
    def __init__(self, node1, node2):
        self.node1: Node = node1
        self.node2: Node = node2


nodes: list[Node] = []
edges = []

lines = open('gtapaths.txt').readlines()
i = 0
for i, line in enumerate(lines):
    tokens = line.split(',')
    if tokens[0].strip() == "end" and len(nodes) > 10:
        break

    if len(tokens) != 1:
        node = Node(tokens[0].strip(), tokens[1].strip(), tokens[2].strip())
        nodes.append(node)

for j, line in enumerate(lines[i::]):
    tokens = line.split(',')
    if tokens[0].strip() == "end" and len(edges) > 10:
        break

    if len(tokens) != 1:
        node1 = nodes[int(tokens[0].strip())]
        node2 = nodes[int(tokens[1].strip())]
        edges.append(NodeEdge(node1, node2))




#for i, node in enumerate(nodes):
    #print(str(i) + '. ' + json.dumps(node.__dict__))