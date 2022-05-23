import copy
import matplotlib.pyplot as plt
from pandas import array
from maze_generator.node import NodeType

class MazeVisual:
    def __init__(self, size_x, size_y, maze):
        self.size_x = size_x
        self.size_y = size_y
        self.maze = maze
        self.maze_array = self.object_to_array(maze)
        self.solution_array = self.draw_solution(self.maze_array)
        self.draw_maze("Maze", self.maze_array)
        self.draw_maze("Maze", self.solution_array)


    def draw_maze(self, name, array):
        plt.figure(figsize=(self.size_x,self.size_y))
        plt.imshow(array, cmap="tab20c")
        plt.title(name)
        plt.show()
    
    
    def object_to_array(self, maze):
        maze_array = []
        for line in maze:
            array = []
            for node in line:
                if(node.type == NodeType.WALL):
                    array.append(20)
                elif(node.type == NodeType.PATH):
                    array.append(0)
                elif(node.type == NodeType.START):
                    array.append(4)
                else:
                    array.append(8)
            maze_array.append(array)
        return maze_array


    def draw_solution(self, maze):
        solution_array = copy.deepcopy(maze)
        for line in range(self.size_x):
            for color in range(self.size_y):
                if(self.maze[line][color].is_passed):
                    solution_array[line][color] = 11
        return solution_array