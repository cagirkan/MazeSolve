from solvers.BFS_Algorithm import Node 
class MazeNode(Node):
  
  def __init__(self, graph, value):
    self.graph = graph
    self.value = value
    self.parent = None

  
  def __eq__(self, other):
    if isinstance(other, MazeNode):
      return self.value == other.value
    return self.value == other

  
  def is_the_solution(self, final_state):
    return self.value == final_state

  
  def extend_node(self):
    children = [MazeNode(self.graph, child) for child in self.graph[self.value]]
    for child in children:
      child.parent = self
    return children

  def _find_path(self):
    path = []
    current_node = self
    while current_node.parent is not None:
      path.insert(0, current_node.value)
      current_node = current_node.parent
    path.insert(0, current_node.value)
    return path

  def __str__(self):
    total_path = self._find_path()
    path = ""
    for index in range(len(total_path)):
      if index == len(total_path) - 1:
        path += f"{total_path[index]} "
      else:
        path += f"{total_path[index]} -> "

    return path + f"\nPath lenght: {len(total_path)-1}"

  def __repr__(self):
      return self._find_path()