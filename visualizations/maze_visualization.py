import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import cm
from colorspacious import cspace_converter
from maze_generator.node import NodeType

class MazeVisual:
    def __init__(self, size_x, size_y, maze):
        self.size_x = size_x
        self.size_y = size_y
        self.maze = maze
        self.maze_array = []
        self.object_to_array()
        self.draw_maze("Maze", self.maze_array)


    def draw_maze(self, name, array):
        plt.figure(figsize=(self.size_x,self.size_y))
        plt.imshow(array, cmap="tab20c")
        plt.title(name)
        plt.show()
    
    
    def object_to_array(self):
        for line in self.maze:
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
            self.maze_array.append(array)