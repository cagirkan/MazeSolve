class DFS_Algo:
    def __init__(self, graph):
        self.visited = []  
        self.graph = graph
        self.solution = self.dfs()


    def dfs_visit(self, vertex):
        if vertex not in self.visited:
            self.visited.append(vertex)
            for nb in self.graph[vertex]:
                self.dfs_visit(nb)

    def dfs(self):
        for ver in self.graph:
            if ver not in self.visited:
                self.dfs_visit(ver)
        return self.visited