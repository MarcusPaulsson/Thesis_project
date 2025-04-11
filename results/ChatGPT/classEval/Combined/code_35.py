from collections import deque


class EightPuzzle:
    """
    This class implements the classic 8-puzzle game, including methods for finding the blank tile,
    making moves, getting possible moves, and solving the puzzle using a breadth-first search algorithm.
    """

    def __init__(self, initial_state):
        """
        Initializes the initial state of the Eight Puzzle Game and sets the goal state.
        :param initial_state: a 3x3 list of integers representing the initial state.
        """
        self.initial_state = initial_state
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def find_blank(self, state):
        """
        Find the blank position of the current state, which is represented by the 0 element.
        :param state: a 3x3 list of integers representing the current state.
        :return: Tuple of (i, j) coordinates of the blank tile, or None if not found.
        """
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return (i, j)
        return None

    def move(self, state, direction):
        """
        Move the blank tile in the specified direction.
        :param state: a 3x3 list of integers representing the state before moving.
        :param direction: str, one of 'up', 'down', 'left', 'right'.
        :return: a new state after the move, or the original state if the move is invalid.
        """
        new_state = [row[:] for row in state]  # Create a deep copy of the state
        blank_i, blank_j = self.find_blank(state)

        if direction == 'up' and blank_i > 0:
            new_state[blank_i][blank_j], new_state[blank_i - 1][blank_j] = new_state[blank_i - 1][blank_j], new_state[blank_i][blank_j]
        elif direction == 'down' and blank_i < 2:
            new_state[blank_i][blank_j], new_state[blank_i + 1][blank_j] = new_state[blank_i + 1][blank_j], new_state[blank_i][blank_j]
        elif direction == 'left' and blank_j > 0:
            new_state[blank_i][blank_j], new_state[blank_i][blank_j - 1] = new_state[blank_i][blank_j - 1], new_state[blank_i][blank_j]
        elif direction == 'right' and blank_j < 2:
            new_state[blank_i][blank_j], new_state[blank_i][blank_j + 1] = new_state[blank_i][blank_j + 1], new_state[blank_i][blank_j]

        return new_state

    def get_possible_moves(self, state):
        """
        Get all possible moves for the current state.
        :param state: a 3x3 list of integers representing the current state.
        :return: a list of possible moving directions.
        """
        moves = []
        blank_i, blank_j = self.find_blank(state)

        if blank_i > 0:
            moves.append('up')
        if blank_i < 2:
            moves.append('down')
        if blank_j > 0:
            moves.append('left')
        if blank_j < 2:
            moves.append('right')

        return moves

    def solve(self):
        """
        Use BFS algorithm to find the path solution from the initial state to the goal state.
        :return: list of string directions that leads to the goal state, or an empty list if unsolvable.
        """
        open_list = deque([(self.initial_state, [])])
        visited = {tuple(map(tuple, self.initial_state))}

        while open_list:
            current_state, path = open_list.popleft()

            if current_state == self.goal_state:
                return path

            for move_direction in self.get_possible_moves(current_state):
                new_state = self.move(current_state, move_direction)
                state_tuple = tuple(map(tuple, new_state))

                if state_tuple not in visited:
                    visited.add(state_tuple)
                    open_list.append((new_state, path + [move_direction]))

        return []
