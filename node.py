from asyncio.windows_events import NULL


class Node:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.neighbours = []
    
    def add_neighbour(self, neighbour):
        self.neighbours.append(neighbour)