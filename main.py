from maze_generator.read_maze import ReadMaze
from solvers.BFS_Algorithm import BFS
from maze_generator.maze import MazeNode
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
  for key, value in graph.items():
    for node in value:
      G.addEdge(key, node)
  G.visualize()

  mazes = MazeNode(graph, "S")
  bfs = BFS(mazes, "I")
  bfs.search()

if __name__ == '__main__':
  main()