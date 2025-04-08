class EightPuzzle:
    """
    This class implements the classic 8-puzzle game, including methods for finding the blank tile,
    making moves, getting possible moves, and solving the puzzle using a breadth-first search algorithm.
    """

    def __init__(self, initial_state):
        """
        Initializes the initial state of the Eight Puzzle Game, and sets the goal state.
        
        :param initial_state: A 3x3 list of integers representing the initial state.
        """
        self.initial_state = initial_state
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def find_blank(self, state):
        """
        Finds the position of the blank tile (0) in the current state.
        
        :param state: A 3x3 list of integers representing the current state.
        :return: Tuple (i, j) representing the coordinates of the blank tile, or None if not found.
        """
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j
        return None

    def move(self, state, direction):
        """
        Moves the blank tile in the specified direction if possible.
        
        :param state: A 3x3 list of integers representing the state before moving.
        :param direction: A string, one of 'up', 'down', 'left', 'right'.
        :return: A new state after the move, or the original state if the move is invalid.
        """
        i, j = self.find_blank(state)
        new_state = [row[:] for row in state]  # Create a copy of the current state

        if direction == 'up' and i > 0:
            new_state[i][j], new_state[i - 1][j] = new_state[i - 1][j], new_state[i][j]
        elif direction == 'down' and i < 2:
            new_state[i][j], new_state[i + 1][j] = new_state[i + 1][j], new_state[i][j]
        elif direction == 'left' and j > 0:
            new_state[i][j], new_state[i][j - 1] = new_state[i][j - 1], new_state[i][j]
        elif direction == 'right' and j < 2:
            new_state[i][j], new_state[i][j + 1] = new_state[i][j + 1], new_state[i][j]
        else:
            return state  # Invalid move

        return new_state

    def get_possible_moves(self, state):
        """
        Returns a list of possible moves based on the current state.
        
        :param state: A 3x3 list of integers representing the current state.
        :return: A list of strings representing possible moves.
        """
        moves = []
        i, j = self.find_blank(state)
        if i > 0: moves.append('up')
        if i < 2: moves.append('down')
        if j > 0: moves.append('left')
        if j < 2: moves.append('right')
        return moves

    def solve(self):
        """
        Solves the puzzle using the breadth-first search (BFS) algorithm.
        
        :return: A list of strings representing the solution moves to reach the goal state.
        """
        from collections import deque

        open_list = deque([(self.initial_state, [])])
        visited = set()

        while open_list:
            current_state, path = open_list.popleft()
            if current_state == self.goal_state:
                return path

            visited.add(tuple(map(tuple, current_state)))

            for move_direction in self.get_possible_moves(current_state):
                new_state = self.move(current_state, move_direction)
                if tuple(map(tuple, new_state)) not in visited:
                    open_list.append((new_state, path + [move_direction]))

        return []