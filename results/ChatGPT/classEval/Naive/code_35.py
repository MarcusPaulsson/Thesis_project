class EightPuzzle:
    """
    This class is an implementation of the classic 8-puzzle game, including methods for finding the blank tile,
    making moves, getting possible moves, and solving the puzzle using a breadth-first search algorithm.
    """

    def __init__(self, initial_state):
        """
        Initializes the initial state of the Eight Puzzle Game and sets the goal state.
        :param initial_state: a 3x3 list of integers representing the initial state
        """
        self.initial_state = initial_state
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def find_blank(self, state):
        """
        Find the blank position (0 element) of the current state.
        :param state: a 3x3 list of integers representing the current state.
        :return: tuple of (i, j) representing coordinates of the blank block.
        """
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j

    def move(self, state, direction):
        """
        Makes a move in the specified direction by swapping the blank block with an adjacent block.
        :param state: a 3x3 list of integers representing the state before moving.
        :param direction: str, direction to move ('up', 'down', 'left', 'right').
        :return: new_state, a 3x3 list of integers representing the state after moving.
        """
        i, j = self.find_blank(state)
        new_state = [row.copy() for row in state]  # Create a copy of the state

        if direction == 'up' and i > 0:
            new_state[i][j], new_state[i - 1][j] = new_state[i - 1][j], new_state[i][j]
        elif direction == 'down' and i < 2:
            new_state[i][j], new_state[i + 1][j] = new_state[i + 1][j], new_state[i][j]
        elif direction == 'left' and j > 0:
            new_state[i][j], new_state[i][j - 1] = new_state[i][j - 1], new_state[i][j]
        elif direction == 'right' and j < 2:
            new_state[i][j], new_state[i][j + 1] = new_state[i][j + 1], new_state[i][j]
        else:
            return state  # No movement possible, return the original state

        return new_state

    def get_possible_moves(self, state):
        """
        Finds all possible moving directions based on the current state.
        :param state: a 3x3 list of integers representing the current state.
        :return: a list of strings representing possible moving directions.
        """
        i, j = self.find_blank(state)
        moves = []

        if i > 0: moves.append('up')
        if i < 2: moves.append('down')
        if j > 0: moves.append('left')
        if j < 2: moves.append('right')

        return moves

    def solve(self):
        """
        Uses BFS algorithm to find the path solution from the initial state to the goal state.
        :return: path, a list of strings representing the solution to reach the goal state.
        """
        from collections import deque

        open_list = deque([(self.initial_state, [])])  # Queue of (state, path)
        visited = set()  # Track visited states

        while open_list:
            current_state, path = open_list.popleft()
            visited.add(tuple(map(tuple, current_state)))  # Add to visited

            if current_state == self.goal_state:
                return path

            for move_direction in self.get_possible_moves(current_state):
                new_state = self.move(current_state, move_direction)
                if tuple(map(tuple, new_state)) not in visited:
                    open_list.append((new_state, path + [move_direction]))

        return []  # Return empty if no solution is found