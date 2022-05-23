from asyncio.windows_events import NULL
from enum import Enum
class NodeType(Enum):
    WALL = 0
    PATH = 1
    START = 2
    TARGET = 3
class Node:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.is_passed = False
        self.neighbours = []
    
    def add_neighbour(self, neighbour):
        self.neighbours.append(neighbour)