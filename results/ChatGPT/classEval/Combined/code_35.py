class EightPuzzle:
    """
    This class implements the classic 8-puzzle game, including methods for finding the blank tile,
    making moves, getting possible moves, and solving the puzzle using a breadth-first search algorithm.
    """

    def __init__(self, initial_state):
        """
        Initialize the initial state of the Eight Puzzle Game and set the goal state.
        :param initial_state: a 3x3 list of integers representing the initial state
        """
        self.initial_state = initial_state
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def find_blank(self, state):
        """
        Find the blank position (0) in the current state.
        :param state: a 3x3 list of integers representing the current state
        :return: tuple (i, j) representing the coordinates of the blank tile, or None if not found
        """
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j
        return None

    def move(self, state, direction):
        """
        Move the blank tile in the specified direction.
        :param state: a 3x3 list of integers representing the current state
        :param direction: str, one of 'up', 'down', 'left', 'right'
        :return: new_state: a 3x3 list of integers representing the new state after the move
        """
        blank_pos = self.find_blank(state)
        if blank_pos is None:
            return state
        
        i, j = blank_pos
        new_state = [row[:] for row in state]  # Create a copy of the current state

        if direction == 'up' and i > 0:
            new_state[i][j], new_state[i - 1][j] = new_state[i - 1][j], new_state[i][j]
        elif direction == 'down' and i < 2:
            new_state[i][j], new_state[i + 1][j] = new_state[i + 1][j], new_state[i][j]
        elif direction == 'left' and j > 0:
            new_state[i][j], new_state[i][j - 1] = new_state[i][j - 1], new_state[i][j]
        elif direction == 'right' and j < 2:
            new_state[i][j], new_state[i][j + 1] = new_state[i][j + 1], new_state[i][j]

        return new_state

    def get_possible_moves(self, state):
        """
        Get all possible moves for the current state.
        :param state: a 3x3 list of integers representing the current state
        :return: list of str representing possible moves
        """
        moves = []
        blank_pos = self.find_blank(state)
        if blank_pos is None:
            return moves
        
        i, j = blank_pos

        if i > 0: moves.append('up')
        if i < 2: moves.append('down')
        if j > 0: moves.append('left')
        if j < 2: moves.append('right')

        return moves

    def solve(self):
        """
        Solve the puzzle using BFS algorithm.
        :return: list of str representing the solution path to the goal state
        """
        from collections import deque

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