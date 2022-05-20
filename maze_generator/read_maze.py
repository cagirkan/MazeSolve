from node import Node, NodeType

nodesMatrix = []
with open('mazes/1.in') as f:
    lines = f.read().splitlines()

coords = lines[0].split(' ')
xLen = int(coords[0])
yLen = int(coords[1])
index = 0
lines.pop(0)

for line in lines:
    nodes = []
    for char in line:
        if(char == 'S'):
            node = Node('S', NodeType.START)
        elif(char == 'T'):
            node = Node('T', NodeType.TARGET)
        elif(char == '.'):
            node = Node(index, NodeType.PATH)
        elif(char == '#'):
            node = Node(index, NodeType.WALL)
        else:
            continue
        nodes.append(node)
        index += 1
    nodesMatrix.append(nodes)

for x in range(xLen - 1):
    if(x == 0):
        continue
    for y in range(yLen - 1):
        if(y == 0):
            continue
        if(nodesMatrix[x][y].type != NodeType.WALL):
            if(nodesMatrix[x][y + 1].type != NodeType.WALL):
                nodesMatrix[x][y].add_neighbour(nodesMatrix[x][y + 1])
            if(nodesMatrix[x][y - 1].type != NodeType.WALL):
                nodesMatrix[x][y].add_neighbour(nodesMatrix[x][y - 1])
            if(nodesMatrix[x + 1][y].type != NodeType.WALL):
                nodesMatrix[x][y].add_neighbour(nodesMatrix[x + 1][y])
            if(nodesMatrix[x - 1][y].type != NodeType.WALL):
                nodesMatrix[x][y].add_neighbour(nodesMatrix[x - 1][y])

for line in nodesMatrix:
    for node in line:
        print(node.name, end =" ")
    print()

for line in nodesMatrix:
    for node in line:
        print(node.type.name, end =" ")
    print()

# for line in nodesMatrix:
#     for node in line:
#         print(f"Neighbours of node{node.name}")
#         for neighbour in node.neighbours:
#             print(neighbour.name, end =" ")
#     print()

graph = {}
for line in nodesMatrix:
    for node in line:
        if(node.type != NodeType.WALL):
            graph[node.name] = []
            for neighbour in node.neighbours:
                graph[node.name].append(neighbour.name)

print(graph)