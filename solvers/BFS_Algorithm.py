from abc import ABC, abstractmethod
class Node(ABC):

  @abstractmethod
  def __eq__(self, other):
    pass

  @abstractmethod
  def is_the_solution(self, state):
    pass

  @abstractmethod
  def extend_node(self):
    pass

  @abstractmethod
  def __str__(self):
    pass

  @abstractmethod
  def __repr__(self):
    pass
  
  

class BFS:
  def __init__(self, start, final):
    self.start_state = start
    self.final_state = final
    self.frontier = [self.start_state]
    self.checked_nodes = []
    self.number_of_steps = 0
    self.path = []
    self.solution = []

  def insert_to_frontier(self, node):
    self.frontier.append(node)
  

  def remove_from_frontier(self):
    first_node = self.frontier.pop(0)
    self.checked_nodes.append(first_node)
    return first_node


  def frontier_is_empty(self):
    if len(self.frontier) == 0:
      return True
    return False

  
  def search(self):
    while True:
      self.number_of_steps += 1
      if self.frontier_is_empty():
        print(f"No Solution Found after {self.number_of_steps} steps!!!")
        break
        
      selected_node = self.remove_from_frontier()

      # check if the selected_node is the solution
      if selected_node.is_the_solution(self.final_state):
        print(f"Solution Found in {self.number_of_steps} steps")
        print(selected_node)
        self.solution = selected_node.__repr__()
        break

      # extend the node
      new_nodes = selected_node.extend_node()

      # add the extended nodes in the frontier
      if len(new_nodes) > 0:
        for new_node in new_nodes:
          if new_node not in self.frontier and new_node not in self.checked_nodes:
            self.insert_to_frontier(new_node)

