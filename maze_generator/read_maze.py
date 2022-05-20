from matplotlib.pyplot import cla
from maze_generator.node import Node, NodeType

class ReadMaze():
    def __init__(self, path):
        self.nodes_matrix = []
        self.lines = self.read_maze("mazes/" + path)
        self.coords = self.lines[0].split(' ')
        self.x_len = int(self.coords[0])
        self.y_len = int(self.coords[1])
        self.graph = {}
        self.lines.pop(0)
        self.initialize_nodes(self.lines)
        self.add_neighbours()
        
        for line in self.nodes_matrix:
            for node in line:
                print(node.name, end =" ")
            print()

        for line in self.nodes_matrix:
            for node in line:
                print(node.type.name, end =" ")
            print()

    
    def read_maze(self, path):
        with open(path) as f:
            return f.read().splitlines()


    def initialize_nodes(self, lines):
        index = 0
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
            self.nodes_matrix.append(nodes)


    def add_neighbours(self):
        for x in range(self.x_len - 1):
            if(x == 0):
                continue
            for y in range(self.y_len - 1):
                if(y == 0):
                    continue
                if(self.nodes_matrix[x][y].type != NodeType.WALL):
                    if(self.nodes_matrix[x][y + 1].type != NodeType.WALL):
                        self.nodes_matrix[x][y].add_neighbour(self.nodes_matrix[x][y + 1])
                    if(self.nodes_matrix[x][y - 1].type != NodeType.WALL):
                        self.nodes_matrix[x][y].add_neighbour(self.nodes_matrix[x][y - 1])
                    if(self.nodes_matrix[x + 1][y].type != NodeType.WALL):
                        self.nodes_matrix[x][y].add_neighbour(self.nodes_matrix[x + 1][y])
                    if(self.nodes_matrix[x - 1][y].type != NodeType.WALL):
                        self.nodes_matrix[x][y].add_neighbour(self.nodes_matrix[x - 1][y])
        for line in self.nodes_matrix:
            for node in line:
                if(node.type != NodeType.WALL):
                    self.graph[node.name] = []
                    for neighbour in node.neighbours:
                        self.graph[node.name].append(neighbour.name)