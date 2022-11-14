class Problem5Solver:
	'''
	All utils used to solve problem 5
	'''

	@staticmethod
	def read_input(file: str) -> list[tuple[int, int, int, int]]:
		'''
		Reads the input file

		Args:
			file (str): The file path

		Returns:
			list[tuple[int, int, int, int]]: List of vent lines
			A vent line is represented as a Tuple with the end
			points coordinates in the following order
			(x1, y1, x2, y2)
		'''
		vent_lines = []
		with open(file, 'r', encoding='utf-8') as input_file:
			for line in input_file:
				points = line.split(' -> ')
				vent_line = tuple(
					int(coord) for point in points
					for coord in point.split(',')
				)
				vent_lines.append(vent_line)

		return vent_lines

	@staticmethod
	def find_grid_size(
		vent_lines: list[tuple[int, int, int, int]]
	) -> tuple[int, int]:
		'''
		Finds the grid size from the list of vent lines

		Args:
			vent_lines (list[tuple[int, int, int, int]]): The
			list of vent lines

		Returns:
			tuple[int, int]: The grid size (x-axis, y-axis)
		'''
		x_max = y_max = 0
		for vent_line in vent_lines:
			if vent_line[0] > x_max:
				x_max = vent_line[0]
			if vent_line[2] > x_max:
				x_max = vent_line[2]
			if vent_line[1] > y_max:
				y_max = vent_line[1]
			if vent_line[3] > y_max:
				y_max = vent_line[3]

		return x_max, y_max

	@staticmethod
	def is_not_diagonal(
		vent_line : tuple[int, int, int, int]
	) -> bool :
		'''
		Checks if the vent line is horizontal or vertical

		Args:
			vent_line (tuple[int, int, int, int]): The vent
			line to check

		Returns:
			bool: True if the line is horizontal or vertical, False
			if it is a diagonal
		'''
		return (
			vent_line[0] == vent_line[2] or vent_line[1] == vent_line[3]
		)

	@staticmethod
	def get_line_points(
		vent_line: tuple[int, int, int, int]
	) -> list[tuple[int, int]]:
		'''
		Get all the points covered by the given line

		Args:
			vent_line (tuple[int, int, int, int]): The given line

		Returns:
			list[tuple[int, int]]: The points covered by the line
		'''
		start_point = (vent_line[0], vent_line[1])
		end_point = (vent_line[2], vent_line[3])
		line_points = [start_point]

		cur_x = start_point[0]
		cur_y = start_point[1]
		end_x = end_point[0]
		end_y = end_point[1]

		if cur_x == end_x:
			# The line is vertical
			if cur_y < end_y:
				# The line goes from left to right
				cur_y += 1
				while cur_y < end_y:
					line_points.append((cur_x, cur_y))
					cur_y += 1
			else:
				# The line goes from right to left
				cur_y -= 1
				while cur_y > end_y:
					line_points.append((cur_x, cur_y))
					cur_y -= 1
		elif cur_y == end_y:
			# The line is horizontal
			if cur_x < end_x:
				# The line goes upwards
				cur_x += 1
				while cur_x < end_x:
					line_points.append((cur_x, cur_y))
					cur_x += 1
			else:
				# The line goes downwards
				cur_x -= 1
				while cur_x > end_x:
					line_points.append((cur_x, cur_y))
					cur_x -= 1
		line_points.append(end_point)

		return line_points

	@staticmethod
	def find_lines_overlap_simple(file: str) -> int:
		'''
		Finds the number of line overlaps considering only
		vertical and horizontal lines (not diagonal ones)

		Args:
			file (str): The input file path

		Returns:
			int: The number of line overlaps considering only
			vertical and horizontal lines
		'''
		vent_lines = Problem5Solver.read_input(file)
		# vent_lines = [(3,4,1,4)]

		covered_points = {}

		for line in vent_lines:
			if Problem5Solver.is_not_diagonal(line):
				# Keep only horizontal and vertical lines
				line_points = Problem5Solver.get_line_points(line)
				for point in line_points:
					# Update the number of overlaps for each point
					nb_overlaps = covered_points.get(point, 0)
					covered_points[point] = nb_overlaps + 1

		# Count number of overlap points
		overlap_points = sum(
			int(overlaps > 1) for overlaps in covered_points.values()
		)

		return overlap_points

	@staticmethod
	def func_part2(file: str) -> None:
		pass

def main() -> None:
	'''
	Main function
	'''
	### First part of the problem
	res1 = Problem5Solver.find_lines_overlap_simple('input')
	print(f'First part result : {res1}')

	### Second part of the problem
	res2 = Problem5Solver.func_part2('input')
	print(f'Second part result : {res2}')

if __name__ == '__main__':
	main()
