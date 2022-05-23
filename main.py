from maze_generator.convert_maze import ConvertMaze
from solvers.BFS_Algorithm import BFS
from maze_generator.maze import MazeNode
from solvers.expand import Expand
from visualizations.Graph_Visualization import GraphVisualization
import networkx as nx
import matplotlib.pyplot as plt

def main():
  # Representation of a graph as a dictionary
  read_graph = ConvertMaze("1.in")
  print(read_graph.graph)
  
  G = GraphVisualization()
  for key, value in read_graph.graph.items():
    for node in value:
      G.add_edge(key, node)
  G.visualize()

  print(read_graph.complete_graph)
  G2 = GraphVisualization()
  for key, value in read_graph.complete_graph.items():
    for node in value:
      G2.add_edge(key, node)
  G2.visualize()

  mazes = MazeNode(read_graph.graph, "S")
  bfs = BFS(mazes, "T")
  bfs.search()
  print(bfs.solution)
  expanded_solution = Expand(bfs.solution, read_graph.complete_graph)
  print(expanded_solution.solution_path)

if __name__ == '__main__':
  main()