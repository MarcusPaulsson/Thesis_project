class EightPuzzle:
    """
    This class is an implementation of the classic 8-puzzle game, including methods for finding the blank tile, making moves, getting possible moves, and solving the puzzle using a breadth-first search algorithm.
    """

    def __init__(self, initial_state):
        """
        Initializes the Eight Puzzle game with the initial state.

        Args:
            initial_state (list[list[int]]): A 3x3 list of integers representing the initial state of the puzzle.
        """
        if not self._is_valid_state(initial_state):
            raise ValueError("Invalid initial state: Must be a 3x3 list of integers 0-8 with no repeats.")

        self.initial_state = [row[:] for row in initial_state]  # Create a deep copy
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def _is_valid_state(self, state):
        """
        Helper function to check if a given state is valid.
        """
        if not isinstance(state, list) or len(state) != 3:
            return False
        for row in state:
            if not isinstance(row, list) or len(row) != 3:
                return False
            for val in row:
                if not isinstance(val, int) or val < 0 or val > 8:
                    return False

        # Check for duplicates
        flattened = [val for row in state for val in row]
        if len(set(flattened)) != 9:
            return False

        return True


    def find_blank(self, state):
        """
        Finds the coordinates of the blank tile (represented by 0) in the given state.

        Args:
            state (list[list[int]]): A 3x3 list of integers representing the puzzle state.

        Returns:
            tuple[int, int]: A tuple (row, col) representing the coordinates of the blank tile.
        """
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j
        return None  # Should never happen in a valid state


    def move(self, state, direction):
        """
        Generates a new state by moving the blank tile in the specified direction.

        Args:
            state (list[list[int]]): A 3x3 list of integers representing the puzzle state.
            direction (str): The direction to move the blank tile ('up', 'down', 'left', 'right').

        Returns:
            list[list[int]] or None: A new state after the move, or None if the move is invalid.
        """
        blank_i, blank_j = self.find_blank(state)
        new_state = [row[:] for row in state]  # Deep copy

        if direction == 'up' and blank_i > 0:
            new_state[blank_i][blank_j], new_state[blank_i - 1][blank_j] = new_state[blank_i - 1][blank_j], new_state[blank_i][blank_j]
            return new_state
        elif direction == 'down' and blank_i < 2:
            new_state[blank_i][blank_j], new_state[blank_i + 1][blank_j] = new_state[blank_i + 1][blank_j], new_state[blank_i][blank_j]
            return new_state
        elif direction == 'left' and blank_j > 0:
            new_state[blank_i][blank_j], new_state[blank_i][blank_j - 1] = new_state[blank_i][blank_j - 1], new_state[blank_i][blank_j]
            return new_state
        elif direction == 'right' and blank_j < 2:
            new_state[blank_i][blank_j], new_state[blank_i][blank_j + 1] = new_state[blank_i][blank_j + 1], new_state[blank_i][blank_j]
            return new_state

        return None  # Invalid move


    def get_possible_moves(self, state):
        """
        Determines the possible moves (directions) from the given state.

        Args:
            state (list[list[int]]): A 3x3 list of integers representing the puzzle state.

        Returns:
            list[str]: A list of possible move directions ('up', 'down', 'left', 'right').
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
        Solves the 8-puzzle using Breadth-First Search (BFS).

        Returns:
            list[str] or None: A list of move directions representing the solution path, or None if no solution is found.
        """
        initial_state_tuple = tuple(tuple(row) for row in self.initial_state)
        goal_state_tuple = tuple(tuple(row) for row in self.goal_state)

        if initial_state_tuple == goal_state_tuple:
            return []  # Already at the goal state

        open_list = [(self.initial_state, [])]  # (state, path)
        visited = {initial_state_tuple}

        while open_list:
            current_state, path = open_list.pop(0)
            current_state_tuple = tuple(tuple(row) for row in current_state)


            possible_moves = self.get_possible_moves(current_state)
            for move in possible_moves:
                new_state = self.move(current_state, move)
                if new_state:
                    new_state_tuple = tuple(tuple(row) for row in new_state)

                    if new_state_tuple == goal_state_tuple:
                        return path + [move]

                    if new_state_tuple not in visited:
                        open_list.append((new_state, path + [move]))
                        visited.add(new_state_tuple)

        return None  # No solution found