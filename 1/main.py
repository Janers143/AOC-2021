class Problem1Solver:
	'''
	All utils used to solve problem 1 
	'''

	@staticmethod
	def find_nb_depth_increases(file: str) -> int:
		'''
		Gets the number of times the depth measurement has increased

		Args:
			file (str): The file containing all inputs

		Returns:
			int: The number of depth measurements increases
		'''
		nb_increases = 0
		with open(file, 'r') as input_file:
			prev_value = float('inf')
			for line in input_file:
				depth = int(line.strip())
				increased = depth > prev_value
				nb_increases += 1 if increased else 0
				prev_value = depth

		return nb_increases

	@staticmethod
	def find_nb_depth_increases_window(file: str) -> int:
		'''
		Finds the number of times the window of the last 3 measurements has increased

		Args:
			file (str): The file containing all inputs

		Returns:
			int: The number of depth measurements depths increases
		'''
		nb_increases = 0
		with open(file, 'r') as input_file:
			window = [float('inf') for _ in range(3)]
			prev_sum = float('inf')
			for line in input_file:
				# Prepare the window
				depth = int(line.strip())
				window.insert(0, depth)
				window.pop()
				new_sum = sum(window)
				
				# Check if the depth increased on average
				increased = (new_sum > prev_sum)
				prev_sum = new_sum

				# Count increases
				nb_increases += 1 if increased else 0

		return nb_increases

if __name__ == '__main__':
	### First part of the problem
	nb_increases = Problem1Solver.find_nb_depth_increases('input')
	print(f'Number of increases : {nb_increases}')

	### Second part of the problem
	nb_window_increase = Problem1Solver.find_nb_depth_increases_window('input')
	print(f'Number of window increases : {nb_window_increase}')
