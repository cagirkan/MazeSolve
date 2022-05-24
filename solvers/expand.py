from matplotlib.pyplot import flag

from maze_generator.node import NodeType


class Expand:
    def __init__(self, solution, complete_graph, maze):
        self.solution = solution
        self.complete_graph = complete_graph
        self.maze = maze
        self.nodes_traversed = []
        self.solution_path = []
        self.flag = False
        self.expanded_graph = self.expand_solution()
        self.mark_as_solved()


    def expand_solution(self):
        for node in range(len(self.solution)):
            if(self.solution[node] == 'T'):
                break
            for k, v in self.complete_graph.items():
                if(self.flag):
                    self.flag = False
                    break
                if(self.solution[node] == k):
                    for neighbour in v:
                        self.nodes_traversed.append(self.solution[node])
                        self.nodes_traversed.append(neighbour)
                        neighbour_count = len(self.complete_graph[neighbour])
                        next_node = self.complete_graph[neighbour]
                        current_node = k
                        while(neighbour_count == 2 and current_node != 'T'):
                            if(next_node[0] not in self.nodes_traversed):
                                current_node = next_node[0]
                            else:
                                current_node = next_node[1]
                            self.nodes_traversed.append(current_node)
                            next_node = self.complete_graph[current_node]
                            neighbour_count = len(next_node)
                        if(current_node == self.solution[node + 1]):
                            self.solution_path.extend(self.nodes_traversed)
                            self.nodes_traversed = []
                            self.flag = True
                            break
                        self.nodes_traversed = []
        self.solution_path.extend(self.solution)
        self.solution_path = list(dict.fromkeys(self.solution_path))
        print(self.solution_path)
    

    def mark_as_solved(self):
        for path in self.solution_path:
            for line in self.maze:
                for node in line:
                    if(path == node.name and node.type == NodeType.PATH):
                        node.is_passed = True