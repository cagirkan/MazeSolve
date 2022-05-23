from maze_generator.read_maze import ReadMaze
from solvers.BFS_Algorithm import BFS
from maze_generator.maze import MazeNode
from solvers.expand import Expand
from visualizations.Graph_Visualization import GraphVisualization
import networkx as nx
import matplotlib.pyplot as plt

def main():
  # Representation of a graph as a dictionary
  read_graph = ReadMaze("1.in")
  print(read_graph.graph)
  graph = {
    "A": ['S'],
    "B": ['C', 'D','S'],
    "C": ['B', 'J'],
    "D": ['B', 'G', 'S'],
    "E": ['G', 'S'],
    "F": ['G', 'H'],
    "G": ['D', 'E', 'F', 'H', 'J'],
    "H": ['F', 'G', 'I'],
    "I": ['H', 'J'],
    "J": ['C', 'G', 'I'],
    "S": ['A', 'B', 'D', 'E']
  }

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