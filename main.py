from solvers.BFS_Algorithm import BFS
from maze_generator.maze import MazeNode
from visualizations.Graph_Visualization import GraphVisualization
import networkx as nx
import matplotlib.pyplot as plt

def main():
  # Representation of a graph as a dictionary
  graph = {12: [13, 23], 13: [14, 12], 14: [15, 13, 25], 15: ['T', 14], 'T': [15], 18: [29], 20: [31], 23: [34, 12], 25: [36, 14], 29: [40, 18], 31: [42, 20], 34: [45, 23], 36: [47, 25], 38: [39, 49], 39: [40, 38], 40: [41, 39, 29], 41: [42, 40], 42: [41, 53, 31], 45: [56, 34], 47: [58, 36], 49: [60, 38], 53: [64, 42], 56: [67, 45], 58: [69, 47], 60: [71, 49], 62: ['S'], 64: [75, 53], 67: [78, 56], 69: [80, 58], 71: [82, 60], 'S': [84, 62], 75: [86, 64], 78: [89, 67], 80: [91, 69], 82: [71], 84: [95, 'S'], 86: [97, 75], 89: [100, 78], 91: [102, 80], 95: [106, 84], 97: [108, 86], 100: [101, 89], 101: [102, 100], 102: [103, 101, 91], 103: [104, 102], 104: [105, 103], 105: [106, 104], 106: [107, 105, 95], 107: [108, 106], 108: [107, 97]}

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