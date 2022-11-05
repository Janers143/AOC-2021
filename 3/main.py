from collections import defaultdict
from typing import Callable


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
				for i, digit in enumerate(line.strip()):
					# Count the number of ones at each
					# bit position
					nb_ones[i] += 1 if digit == '1' else 0

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
		'''
		Gets the life support rating by multiplying
		the oxygen generator rating times the CO2 scrubber
		rating

		Args:
			file (str): The input file path

		Returns:
			int: The product of the oxygen generator rating
			and the CO2 scrubber rating
		'''
		with open(file, 'r', encoding='utf-8') as input_file:
			all_values = [val.strip() for val in input_file.readlines()]

		# First get the Oxygen generator rating
		index = 0
		# While there's more than 1 value
		values = all_values.copy()
		nb_values = len(values)
		while nb_values > 1:
			# Count the number of '1' at position {bit}
			nb_ones = 0
			for val in values:
				nb_ones += 1 if val[index] == '1' else 0

			if nb_ones >= nb_values / 2 :
				# Then '1' is the most common bit
				# Keep the values whose {index} bit is a '1'
				values = Problem3Solver.__keep_expected_val(
					'1', values, index)
			else :
				# Then '0' is the most common bit
				# Keep the values whose {index} bit is a '0'
				values = Problem3Solver.__keep_expected_val(
					'0', values, index)

			index += 1
			nb_values = len(values)
		oxygen_generator_rating_bin = values[0]
		oxygen_generator_rating = int(
			oxygen_generator_rating_bin, base=2
		)

		# Then get the CO2 Scrubber rating
		index = 0
		# While there's more than 1 value
		values = all_values.copy()
		nb_values = len(values)
		while nb_values > 1:
			# Count the number of '1' at position {bit}
			nb_ones = 0
			for val in values:
				nb_ones += 1 if val[index] == '1' else 0

			if nb_ones >= nb_values / 2 :
				# Then '0' is the least common bit
				# Keep the values whose {index} bit is a '0'
				values = Problem3Solver.__keep_expected_val(
					'0', values, index)
			else :
				# Then '1' is the least common bit
				# Keep the values whose {index} bit is a '0'
				values = Problem3Solver.__keep_expected_val(
					'1', values, index)

			index += 1
			nb_values = len(values)
		co2_scrubber_rating_bin = values[0]
		co2_scrubber_rating = int(
			co2_scrubber_rating_bin, base=2
		)

		return oxygen_generator_rating * co2_scrubber_rating

	@staticmethod
	def __keep_expected_val(
		val: str,
		values: list[str],
		pos: int
	) -> list[str]:
		'''
		Takes a list of binary numbers and keeps only
		the elements whose {pos}th bit is equal to the
		given expected value

		Args:
			val (str): The given expected value
			values (list[str]): The list of binary numbers
			pos (int): The bit index to check

		Returns:
			list[str]: The list of values that fit the
			condition
		'''
		is_expected_val: 'Callable[[str], bool]'= (
			lambda x: x[pos] == val
		)
		kept_values = list(filter(is_expected_val, values))
		return kept_values

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
