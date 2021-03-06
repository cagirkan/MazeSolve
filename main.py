from maze_generator.convert_maze import ConvertMaze
from maze_generator.create_maze import CreateMaze
from solvers.BFS_Algorithm import BFS
from solvers.DFS_Algorithm import DFS_Algo
from maze_generator.maze import MazeNode
from solvers.expand import Expand
from visualizations.Graph_Visualization import GraphVisualization
from visualizations.maze_visualization import MazeVisual

def main():
  # Representation of a graph as a dictionary

  height=int(input("Enter a maze height: "))
  width=int(input("Enter a maze width: "))
  CreateMaze(height,width)
  read_graph = ConvertMaze("maze.in")

  G = GraphVisualization()
  for key, value in read_graph.complete_graph.items():
    for node in value:
      G.add_edge(key, node)
  G.visualize("Graph Of Maze")

  G = GraphVisualization()
  for key, value in read_graph.graph.items():
    for node in value:
      G.add_edge(key, node)
  G.visualize("Simplified Version Of Graph")


  mazes = MazeNode(read_graph.graph, "S")
  bfs = BFS(mazes, "T")
  bfs.search()
  # dfs = DFS_Algo(read_graph.complete_graph)
  # print(dfs.solution)
  Expand(bfs.solution, read_graph.complete_graph, read_graph.nodes_matrix)
  MazeVisual(read_graph.x_len, read_graph.y_len, read_graph.nodes_matrix)

if __name__ == '__main__':
  main()