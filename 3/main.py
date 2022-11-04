from collections import defaultdict


class Problem3Solver:
	'''
	All utils used to solve problem 3
	'''

	@staticmethod
	def get_power_consumption(file: str) -> int:
		'''
		Gets the submarine power consumption by
		calculating the gamma rate and epsilon rate

		Args:
			file (str): The input file path

		Returns:
			int: The product of the gamma rate and
				the epsilon rate
		'''
		with open(file, 'r', encoding='utf-8') as input_file:
			nb_lines = 0
			nb_ones = {}
			nb_ones = defaultdict(lambda: 0, nb_ones)
			for line in input_file:
				# For each binary number, check bit by bit
				nb_lines += 1
				for i, letter in enumerate(line.strip()):
					# Count the number of ones at each
					# bit position
					nb_ones[i] += 1 if letter == '1' else 0

			# Calculate both the gamma and epsilon rate value
			gamma_rate_str = ''
			epsilon_rate_str = ''
			for k in nb_ones.keys():
				more_ones = (nb_ones.get(k) > nb_lines / 2)
				gamma_rate_str += '1' if more_ones else '0'
				epsilon_rate_str += '0' if more_ones else '1'

			gamma_rate = int(gamma_rate_str, base=2)
			epsilon_rate = int(epsilon_rate_str, base=2)

		return gamma_rate * epsilon_rate

	@staticmethod
	def get_life_support_rating(file: str) -> int:
		return 0

def main() -> None:
	'''
	Main function
	'''
	### First part of the problem
	res1 = Problem3Solver.get_power_consumption('input')
	print(f'First part result : {res1}')

	### Second part of the problem
	res2 = Problem3Solver.get_life_support_rating('input')
	print(f'Second part result : {res2}')

if __name__ == '__main__':
	main()
