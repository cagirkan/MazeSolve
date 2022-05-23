from matplotlib.pyplot import flag


class Expand:
    def __init__(self, solution, complete_graph):
        self.solution = solution
        self.complete_graph = complete_graph
        self.nodes_traversed = []
        self.solution_path = []
        self.flag = False
        self.expanded_graph = self.expand_solution()


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
                        while(neighbour_count == 2):
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
        self.solution_path = list(dict.fromkeys(self.solution_path))