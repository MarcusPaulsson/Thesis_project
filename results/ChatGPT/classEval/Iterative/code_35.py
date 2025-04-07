class EightPuzzle:
    """
    This class is an implementation of the classic 8-puzzle game, including methods for finding the blank tile, making moves,
    getting possible moves, and solving the puzzle using a breadth-first search algorithm.
    """

    def __init__(self, initial_state):
        """
        Initialize the initial state of Eight Puzzle Game, stores in attribute self.initial_state.
        Set the goal state of this game, stores in self.goal_state. The size is 3x3.
        :param initial_state: a 3x3 list of integers, stores the initial state
        """
        self.initial_state = initial_state
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def find_blank(self, state):
        """
        Find the blank position (0) in the current state.
        :param state: a 3x3 list of integers, stores the current state.
        :return: tuple (i, j) representing the coordinates of the blank block, or None if not found.
        """
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j
        return None

    def move(self, state, direction):
        """
        Move the blank block in the specified direction.
        :param state: a 3x3 list of integers, stores the state before moving.
        :param direction: str, one of 'up', 'down', 'left', 'right'
        :return: new_state: a 3x3 list of integers, stores the state after moving.
        """
        blank_i, blank_j = self.find_blank(state)
        new_state = [row[:] for row in state]  # Create a copy of the current state

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
        Get all possible moving directions based on the current state.
        :param state: a 3x3 list of integers, stores the current state.
        :return: list of str, possible moving directions.
        """
        blank_i, blank_j = self.find_blank(state)
        moves = []

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
        Use BFS algorithm to find the path from the initial state to the goal state.
        :return: list of str, the solution to reach the goal state.
        """
        from collections import deque

        open_list = deque([(self.initial_state, [])])
        visited = set()
        visited.add(tuple(map(tuple, self.initial_state)))

        while open_list:
            current_state, path = open_list.popleft()

            if current_state == self.goal_state:
                return path

            possible_moves = self.get_possible_moves(current_state)

            for move_direction in possible_moves:
                new_state = self.move(current_state, move_direction)
                state_tuple = tuple(map(tuple, new_state))

                if state_tuple not in visited:
                    visited.add(state_tuple)
                    open_list.append((new_state, path + [move_direction]))

        return None