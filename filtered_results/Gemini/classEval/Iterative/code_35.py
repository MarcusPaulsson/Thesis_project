from collections import deque

class EightPuzzle:
    """
    This class is an implementation of the classic 8-puzzle game, including methods for finding the blank tile, making moves, getting possible moves, and solving the puzzle using a breadth-first search algorithm.
    """

    def __init__(self, initial_state):
        """
        Initializing the initial state of Eight Puzzle Game, stores in attribute self.initial_state.
        And set the goal state of this game, stores in self.goal_state. In this case, set the size as 3*3
        :param initial_state: a 3*3 size list of Integer, stores the initial state
        """
        self.initial_state = initial_state
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        self.size = 3

    def find_blank(self, state):
        """
        Find the blank position of current state, which is the 0 element.
        :param state: a 3*3 size list of Integer, stores the current state.
        :return i, j: two Integers, represent the coordinate of the blank block.
        """
        for i in range(self.size):
            for j in range(self.size):
                if state[i][j] == 0:
                    return i, j
        return None

    def move(self, state, direction):
        """
        Find the blank block, then makes the board moves forward the given direction.
        :param state: a 3*3 size list of Integer, stores the state before moving.
        :param direction: str, only has 4 direction 'up', 'down', 'left', 'right'
        :return new_state: a 3*3 size list of Integer, stores the state after moving.
        """
        blank_row, blank_col = self.find_blank(state)
        if blank_row is None or blank_col is None:
            return state

        new_state = [row[:] for row in state]  # Create a copy of the state

        if direction == 'up':
            if blank_row > 0:
                new_state[blank_row][blank_col], new_state[blank_row - 1][blank_col] = new_state[blank_row - 1][blank_col], new_state[blank_row][blank_col]
            else:
                return state
        elif direction == 'down':
            if blank_row < self.size - 1:
                new_state[blank_row][blank_col], new_state[blank_row + 1][blank_col] = new_state[blank_row + 1][blank_col], new_state[blank_row][blank_col]
            else:
                return state
        elif direction == 'left':
            if blank_col > 0:
                new_state[blank_row][blank_col], new_state[blank_row][blank_col - 1] = new_state[blank_row][blank_col - 1], new_state[blank_row][blank_col]
            else:
                return state
        elif direction == 'right':
            if blank_col < self.size - 1:
                new_state[blank_row][blank_col], new_state[blank_row][blank_col + 1] = new_state[blank_row][blank_col + 1], new_state[blank_row][blank_col]
            else:
                return state
        
        return new_state

    def get_possible_moves(self, state):
        """
        According the current state, find all the possible moving directions. Only has 4 direction 'up', 'down', 'left', 'right'.
        :param state: a 3*3 size list of Integer, stores the current state.
        :return moves: a list of str, store all the possible moving directions according to the current state.
        """
        blank_row, blank_col = self.find_blank(state)
        moves = []
        if blank_row is None or blank_col is None:
            return moves

        if blank_row > 0:
            moves.append('up')
        if blank_row < self.size - 1:
            moves.append('down')
        if blank_col > 0:
            moves.append('left')
        if blank_col < self.size - 1:
            moves.append('right')

        return moves

    def solve(self):
        """
        Use BFS algorithm to find the path solution which makes the initial state to the goal method.
        Maintain a list as a queue, named as open_list, append the initial state.
        Always visit and pop the 0 index element, invoke get_possible_moves method find all the possible directions.
        Traversal the possible_moves list and invoke move method to get several new states.Then append them.
        redo the above steps until the open_list is empty or the state has changed to the goal state.
        :return path: list of str, the solution to the goal state.
        """
        if not any(0 in row for row in self.initial_state for row in self.initial_state):
            if self.initial_state == self.goal_state:
                return []
            else:
                return None
        
        if self.initial_state == self.goal_state:
            return []

        initial_state_tuple = tuple(tuple(row) for row in self.initial_state)
        queue = deque([(self.initial_state, [])])
        visited = {initial_state_tuple}

        while queue:
            current_state, path = queue.popleft()

            if current_state == self.goal_state:
                return path

            possible_moves = self.get_possible_moves(current_state)

            for move in possible_moves:
                new_state = self.move(current_state, move)
                new_state_tuple = tuple(tuple(row) for row in new_state)

                if new_state_tuple not in visited:
                    visited.add(new_state_tuple)
                    queue.append((new_state, path + [move]))

        return None  # No solution found