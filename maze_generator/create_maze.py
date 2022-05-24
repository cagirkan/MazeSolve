# Maze generator -- Randomized Prim Algorithm

## Imports
import random
class CreateMaze():
	def __init__(self, height, width):
		self.height = height
		self.width = width
		self.maze = []
		self.create(self.height, self.width, self.maze)
		self.write_file(self.maze)
       
	## Functions
	def print_maze(self, maze):
		for i in range(0, self.height):
			for j in range(0, self.width):
				if (maze[i][j] == 'u'):
					print( str(maze[i][j]), end=" ")
				elif (maze[i][j] == '.'):
					print( str(maze[i][j]), end=" ")
				else:
					print( str(maze[i][j]), end=" ")
				
			print('\n')

	# Find number of surrounding cells
	def surrounding_cells(self, rand_wall):
		s_cells = 0
		if (self.maze[rand_wall[0]-1][rand_wall[1]] == '.'):
			s_cells += 1
		if (self.maze[rand_wall[0]+1][rand_wall[1]] == '.'):
			s_cells += 1
		if (self.maze[rand_wall[0]][rand_wall[1]-1] == '.'):
			s_cells +=1
		if (self.maze[rand_wall[0]][rand_wall[1]+1] == '.'):
			s_cells += 1

		return s_cells

	def create(self, height, width, maze):	
		## Main code
		# Init variables
		wall = '#'
		cell = '.'
		unvisited = 'u'

		# Denote all cells as unvisited
		for i in range(0, height):
			line = []
			for j in range(0, width):
				line.append(unvisited)
			maze.append(line)

		# Randomize starting point and set it a cell
		starting_height = int(random.random()*height)
		starting_width = int(random.random()*width)
		if (starting_height == 0):
			starting_height += 1
		if (starting_height == height-1):
			starting_height -= 1
		if (starting_width == 0):
			starting_width += 1
		if (starting_width == width-1):
			starting_width -= 1

		# Mark it as cell and add surrounding walls to the list
		maze[starting_height][starting_width] = cell
		walls = []
		walls.append([starting_height - 1, starting_width])
		walls.append([starting_height, starting_width - 1])
		walls.append([starting_height, starting_width + 1])
		walls.append([starting_height + 1, starting_width])

		# Denote walls in maze
		maze[starting_height-1][starting_width] = '#'
		maze[starting_height][starting_width - 1] = '#'
		maze[starting_height][starting_width + 1] = '#'
		maze[starting_height + 1][starting_width] = '#'

		while (walls):
			# Pick a random wall
			rand_wall = walls[int(random.random()*len(walls))-1]

			# Check if it is a left wall
			if (rand_wall[1] != 0):
				if (maze[rand_wall[0]][rand_wall[1]-1] == 'u' and maze[rand_wall[0]][rand_wall[1]+1] == '.'):
					# Find the number of surrounding cells
					s_cells = self.surrounding_cells(rand_wall)

					if (s_cells < 2):
						# Denote the new path
						maze[rand_wall[0]][rand_wall[1]] = '.'

						# Mark the new walls
						# Upper cell
						if (rand_wall[0] != 0):
							if (maze[rand_wall[0]-1][rand_wall[1]] != '.'):
								maze[rand_wall[0]-1][rand_wall[1]] = '#'
							if ([rand_wall[0]-1, rand_wall[1]] not in walls):
								walls.append([rand_wall[0]-1, rand_wall[1]])


						# Bottom cell
						if (rand_wall[0] != height-1):
							if (maze[rand_wall[0]+1][rand_wall[1]] != '.'):
								maze[rand_wall[0]+1][rand_wall[1]] = '#'
							if ([rand_wall[0]+1, rand_wall[1]] not in walls):
								walls.append([rand_wall[0]+1, rand_wall[1]])

						# Leftmost cell
						if (rand_wall[1] != 0):	
							if (maze[rand_wall[0]][rand_wall[1]-1] != '.'):
								maze[rand_wall[0]][rand_wall[1]-1] = '#'
							if ([rand_wall[0], rand_wall[1]-1] not in walls):
								walls.append([rand_wall[0], rand_wall[1]-1])
					

					# Delete wall
					self.delete_wall(walls, rand_wall)
					continue

			# Check if it is an upper wall
			if (rand_wall[0] != 0):
				if (maze[rand_wall[0]-1][rand_wall[1]] == 'u' and maze[rand_wall[0]+1][rand_wall[1]] == '.'):

					s_cells = self.surrounding_cells(rand_wall)
					if (s_cells < 2):
						# Denote the new path
						maze[rand_wall[0]][rand_wall[1]] = '.'

						# Mark the new walls
						# Upper cell
						if (rand_wall[0] != 0):
							if (maze[rand_wall[0]-1][rand_wall[1]] != '.'):
								maze[rand_wall[0]-1][rand_wall[1]] = '#'
							if ([rand_wall[0]-1, rand_wall[1]] not in walls):
								walls.append([rand_wall[0]-1, rand_wall[1]])

						# Leftmost cell
						if (rand_wall[1] != 0):
							if (maze[rand_wall[0]][rand_wall[1]-1] != '.'):
								maze[rand_wall[0]][rand_wall[1]-1] = '#'
							if ([rand_wall[0], rand_wall[1]-1] not in walls):
								walls.append([rand_wall[0], rand_wall[1]-1])

						# Rightmost cell
						if (rand_wall[1] != width-1):
							if (maze[rand_wall[0]][rand_wall[1]+1] != '.'):
								maze[rand_wall[0]][rand_wall[1]+1] = '#'
							if ([rand_wall[0], rand_wall[1]+1] not in walls):
								walls.append([rand_wall[0], rand_wall[1]+1])

					# Delete wall
					self.delete_wall(walls, rand_wall)
					continue

			# Check the bottom wall
			if (rand_wall[0] != height-1):
				if (maze[rand_wall[0]+1][rand_wall[1]] == 'u' and maze[rand_wall[0]-1][rand_wall[1]] == '.'):

					s_cells = self.surrounding_cells(rand_wall)
					if (s_cells < 2):
						# Denote the new path
						maze[rand_wall[0]][rand_wall[1]] = '.'

						# Mark the new walls
						if (rand_wall[0] != height-1):
							if (maze[rand_wall[0]+1][rand_wall[1]] != '.'):
								maze[rand_wall[0]+1][rand_wall[1]] = '#'
							if ([rand_wall[0]+1, rand_wall[1]] not in walls):
								walls.append([rand_wall[0]+1, rand_wall[1]])
						if (rand_wall[1] != 0):
							if (maze[rand_wall[0]][rand_wall[1]-1] != '.'):
								maze[rand_wall[0]][rand_wall[1]-1] = '#'
							if ([rand_wall[0], rand_wall[1]-1] not in walls):
								walls.append([rand_wall[0], rand_wall[1]-1])
						if (rand_wall[1] != width-1):
							if (maze[rand_wall[0]][rand_wall[1]+1] != '.'):
								maze[rand_wall[0]][rand_wall[1]+1] = '#'
							if ([rand_wall[0], rand_wall[1]+1] not in walls):
								walls.append([rand_wall[0], rand_wall[1]+1])

					# Delete wall
					self.delete_wall(walls, rand_wall)
					continue

			# Check the right wall
			if (rand_wall[1] != width-1):
				if (maze[rand_wall[0]][rand_wall[1]+1] == 'u' and maze[rand_wall[0]][rand_wall[1]-1] == '.'):

					s_cells = self.surrounding_cells(rand_wall)
					if (s_cells < 2):
						# Denote the new path
						maze[rand_wall[0]][rand_wall[1]] = '.'

						# Mark the new walls
						if (rand_wall[1] != width-1):
							if (maze[rand_wall[0]][rand_wall[1]+1] != '.'):
								maze[rand_wall[0]][rand_wall[1]+1] = '#'
							if ([rand_wall[0], rand_wall[1]+1] not in walls):
								walls.append([rand_wall[0], rand_wall[1]+1])
						if (rand_wall[0] != height-1):
							if (maze[rand_wall[0]+1][rand_wall[1]] != '.'):
								maze[rand_wall[0]+1][rand_wall[1]] = '#'
							if ([rand_wall[0]+1, rand_wall[1]] not in walls):
								walls.append([rand_wall[0]+1, rand_wall[1]])
						if (rand_wall[0] != 0):	
							if (maze[rand_wall[0]-1][rand_wall[1]] != '.'):
								maze[rand_wall[0]-1][rand_wall[1]] = '#'
							if ([rand_wall[0]-1, rand_wall[1]] not in walls):
								walls.append([rand_wall[0]-1, rand_wall[1]])

					# Delete wall
					self.delete_wall(walls, rand_wall)
					continue

			# Delete the wall from the list anyway
			self.delete_wall(walls, rand_wall)
			
		# Mark the remaining unvisited cells as walls
		self.make_walls(width, height)

		# Set start and end
		self.create_start_end(width, height)

	def delete_wall(self, walls, rand_wall):
		for wall in walls:
			if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
				walls.remove(wall)

	def make_walls(self, width, height):
		for i in range(0, height):
			for j in range(0, width):
				if (self.maze[i][j] == 'u'):
					self.maze[i][j] = '#'

	def create_start_end(self, width, height):
		for i in range(0, width):
			if (self.maze[1][i] == '.'):
				self.maze[1][i] = 'S'
				break
		for i in range(width-1, 0, -1):
			if (self.maze[height-2][i] == '.'):
				self.maze[height-2][i] = 'T'
				break

	def write_file(self, maze):
		with open("mazes/maze.in", "w") as f:
			f.write(str(self.height)+ " " +str(self.width)+'\n')
			for i in range(0, self.height):
				for j in range(0, self.width):
					if (maze[i][j] == 'u'):
						f.write(str(maze[i][j]))
					elif (maze[i][j] == '.'):
						f.write(str(maze[i][j]))
					else:
						f.write(str(maze[i][j]))
				f.write('\n')

			