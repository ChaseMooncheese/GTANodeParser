import json


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
safeNodes: list[int] = []

lines = open('gtapaths.txt').readlines()
i = 0  # Declares i in global scope so that the edges loop knows where to start

# Parse all nodes
for i, line in enumerate(lines):
    tokens = line.split(',')
    # Continue until finding the "end" that represents the end of the nodes
    # Verifies that len > 10 because there is an early 'end' on the 3rd line
    if tokens[0].strip() == "end" and len(nodes) > 10:
        break

    # Only add a node on lines that have more than 1 token. Lines with 1 token are keywords that do not define nodes
    if len(tokens) != 1:
        node = Node(float(tokens[0].strip()), float(tokens[1].strip()), float(tokens[2].strip()))
        nodes.append(node)
        if int(tokens[4]) == 0:
            safeIndex: int = len(nodes) - 1
            safeNodes.append(int(safeIndex))

# Parse all edges
for j, line in enumerate(lines[i::]):  # Splice list of lines to start off where the node list ended
    tokens = line.split(',')

    # Continue until finding the "end" that represents the end of the edges
    if tokens[0].strip() == "end" and len(edges) > 10:
        break

    if len(tokens) != 1:    # skip all the 1 word lines (they don't represent edges)
        node1 = int(tokens[0].strip())
        node2 = int(tokens[1].strip())
        edges.append(NodeEdge(node1, node2))


# Convert nodes and edges to dictionaries so they can be formatted as JSON
nodeDicts = [node.__dict__ for node in nodes]
edgeDicts = [edge.__dict__ for edge in edges]

# Combine nodes and edges into one dictionary that can be formatted in JSON
dict = {
    "Nodes": nodeDicts,
    "Edges": edgeDicts
}
output = json.dumps(dict)

# Write output to file
f = open("output.txt", "w")
f.write(output)
f.close()
print('successful')
print('Total Nodes: ' + str(len(nodes)))
print('Total Edges: ' + str(len(edges)))

f2 = open("safe-nodes.txt", "w")
f2.write(json.dumps(safeNodes))
f2.close()

print("Total Safe Nodes: " + str(len(safeNodes)))


