from typing import Tuple


class Board:
	'''
	Model for the bingo board
	'''
	def __init__(self, board_str: list[str]) -> None:
		self.board = Board.__read_board(board_str)

	@staticmethod
	def __read_board(board_str: list[str]) -> list[list[int]]:
		'''
		Reads a five lines string defining the bingo board

		Args:
			board_str (list[str]): The bingo board string
			representation

		Returns:
			list[list[int]]: The board as a list of ints
		'''
		board = []
		for line in board_str:
			int_line = [int(nb) for nb in line.split()]
			board.append(int_line)
		return board

	def get_board(self) -> list[list[int]]:
		'''
		Board getter

		Returns:
			list[list[int]]: The board as a list of ints
		'''
		return self.board

	def mark_number(self, x: int) -> None:
		'''
		Marks a number on the board by replacing it by
		None value

		Args:
			x (int): The value to matrk on the board
		'''
		for line in self.board:
			if x in line:
				line[line.index(x)] = None

	def is_bingo(self) -> bool:
		'''
		Checks if Bingo can be called with this board

		Returns:
			bool: True if there's bingo, False elsewise
		'''
		return self.__full_line() or self.__full_column()

	def __full_line(self) -> bool:
		'''
		Checks if ther's a line in the board full of None

		Returns:
			bool: True if there's an empty line
		'''
		for line in self.board:
			if all(nb is None for nb in line):
				return True
		return False

	def __full_column(self) -> bool:
		'''
		Checks is there's a column in the board full of None

		Returns:
			bool: True if there's an empty column
		'''
		for column in range(5):
			if all(line[column] is None for line in self.board):
				return True
		return False

	def sum_unmarked_numbers(self) -> int:
		'''
		Calculates the sum of all remaining unmarked numbers

		Returns:
			int: The sum result
		'''
		# Function that calculates an int list sum
		# ignoring the None values
		sum_without_none = ( lambda x :
			sum([nb for nb in x if nb])
		)

		return sum([sum_without_none(line) for line in self.board])


class Problem4Solver:
	'''
	All utils used to solve problem 4
	'''
	@staticmethod
	def read_input(file: str) -> Tuple[list[int], list[Board]]:
		'''
		Reads the input file

		Args:
			file (str): The input file

		Returns:
			Tuple[list[int], list[Board]]: The list of drawn
			numbers and the list of available boards
		'''
		with open(file, 'r', encoding='utf-8') as input_file:
			drawn_numbers = [
				int(nb) for nb in input_file.readline().strip().split(',')
			]

			line = input_file.readline()
			boards: list[Board] = []
			board = []
			while line:
				if line != '\n':
					board.append(line.strip())

				if len(board) == 5:
					# We have a new board
					boards.append(Board(board))
					board = []

				line = input_file.readline()

		return drawn_numbers, boards

	@staticmethod
	def get_winning_board(file: str) -> int:
		'''
		Gets the winning board and as a result multiplies the
		sum of the remaining unmarked numbers on the board
		times the last drawn number

		Args:
			file (str): The input file

		Returns:
			int: The product of the sum of the remaining
			unmarked numbers on the board and the last
			drawn number
		'''
		drawn_numbers, boards = Problem4Solver.read_input(file)

		# Go through each drawn number and mark it on all
		# the boards
		for nb in drawn_numbers:
			for brd in boards:
				brd.mark_number(nb)
				if brd.is_bingo():
					# Winner board was found, return the product
					# of the board remaining unmarked numbers sum
					# and the last drawn nb
					return brd.sum_unmarked_numbers() * nb

		error_msg = (
			'No board can call bingo with the given drawn numbers'
		)
		raise Exception(error_msg)

	@staticmethod
	def get_losing_board(file: str) -> int:
		'''
		Gets the losing board (the last one to call bingo)
		and as a result multiplies the sum of the remaining
		unmarked numbers on the board times the last drawn
		number

		Args:
			file (str): The input file

		Returns:
			int: The product of the sum of the remaining
			unmarked numbers on the board and the last
			drawn number
		'''
		drawn_numbers, boards = Problem4Solver.read_input(file)

		# Go through each drawn number and mark it on all
		# the boards
		for nb in drawn_numbers:
			for brd in boards.copy():
				brd.mark_number(nb)
				if brd.is_bingo():
					# The board can call bingo : the board
					# is removed from the list of remaining
					# boards
					boards.remove(brd)
				if not boards:
					# There's no more boards left so the last
					# one to be removed is the losing one
					# Return the product of the board remaining
					# unmarked numbers sum and the last drawn nb
					return brd.sum_unmarked_numbers() * nb

		error_msg = (
			'There is at least one board that can not call bingo'
		)
		raise Exception(error_msg)

def main() -> None:
	'''
	Main function
	'''

	### First part of the problem
	res1 = Problem4Solver.get_winning_board('input')
	print(f'First part result : {res1}')

	### Second part of the problem
	res2 = Problem4Solver.get_losing_board('input')
	print(f'Second part result : {res2}')

if __name__ == '__main__':
	main()
