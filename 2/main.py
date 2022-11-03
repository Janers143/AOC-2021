class Problem2Solver:
	'''
	All utils used to solve problem 2
	'''

	@staticmethod
	def get_position_multiplication(file: str) -> int:
		'''
		Gets the final horizontal position and depth
		Multiply both values to get the expected result

		Args:
			file (str): The input file path

		Returns:
			int: The product of the horizontal position
				and the depth
		'''

		depth = 0
		horizontal_position = 0
		with open(file, 'r', encoding='utf-8') as input_file:
			for line in input_file:
				move, dist = line.split()
				dist = int(dist)

				match move:
					case 'forward':
						horizontal_position += dist
					case 'up':
						depth -= dist
					case 'down':
						depth += dist
					case _:
						raise Exception(f'Could not get next move : {move}')

		return depth * horizontal_position

	@staticmethod
	def get_position_multiplication_with_aim(file: str) -> int:
		'''
		Gets the final horizontal position and depth
		This time when moving up and down the submarine
		aim changes, not the depth
		Multiply both values to get the expected result

		Args:
			file (str): The input file path

		Returns:
			int: The product of the horizontal position
				and the depth
		'''
		depth = 0
		horizontal_position = 0
		aim = 0

		with open(file, 'r', encoding='utf-8') as input_file:
			for line in input_file:
				move, dist = line.split()
				dist = int(dist)

				match move:
					case 'forward':
						horizontal_position += dist
						depth += aim * dist
					case 'down':
						aim += dist
					case 'up':
						aim -= dist
					case _:
						raise Exception(f'Could not get next move : {move}')

		return depth * horizontal_position

def main():
	'''
	Main function
	'''
	### First part of the problem
	res1 = Problem2Solver.get_position_multiplication('input')
	print(f'First part result : {res1}')

	### Second part of the problem
	res2 = Problem2Solver.get_position_multiplication_with_aim('input')
	print(f'Second part result : {res2}')

if __name__ == '__main__':
	main()
