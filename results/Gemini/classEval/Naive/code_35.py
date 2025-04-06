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

    def find_blank(self, state):
        """
        Find the blank position of current state, which is the 0 element.
        :param state: a 3*3 size list of Integer, stores the current state.
        :return i, j: two Integers, represent the coordinate of the blank block.
        """
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j

    def move(self, state, direction):
        """
        Find the blank block, then makes the board moves forward the given direction.
        :param state: a 3*3 size list of Integer, stores the state before moving.
        :param direction: str, only has 4 direction 'up', 'down', 'left', 'right'
        :return new_state: a 3*3 size list of Integer, stores the state after moving.
        """
        blank_row, blank_col = self.find_blank(state)
        new_state = [row[:] for row in state]  # Create a copy to avoid modifying the original state

        if direction == 'up':
            if blank_row > 0:
                new_state[blank_row][blank_col], new_state[blank_row - 1][blank_col] = new_state[blank_row - 1][blank_col], new_state[blank_row][blank_col]
                return new_state
        elif direction == 'down':
            if blank_row < 2:
                new_state[blank_row][blank_col], new_state[blank_row + 1][blank_col] = new_state[blank_row + 1][blank_col], new_state[blank_row][blank_col]
                return new_state
        elif direction == 'left':
            if blank_col > 0:
                new_state[blank_row][blank_col], new_state[blank_row][blank_col - 1] = new_state[blank_row][blank_col - 1], new_state[blank_row][blank_col]
                return new_state
        elif direction == 'right':
            if blank_col < 2:
                new_state[blank_row][blank_col], new_state[blank_row][blank_col + 1] = new_state[blank_row][blank_col + 1], new_state[blank_row][blank_col]
                return new_state

        return None  # Invalid move

    def get_possible_moves(self, state):
        """
        According the current state, find all the possible moving directions. Only has 4 direction 'up', 'down', 'left', 'right'.
        :param state: a 3*3 size list of Integer, stores the current state.
        :return moves: a list of str, store all the possible moving directions according to the current state.
        """
        blank_row, blank_col = self.find_blank(state)
        moves = []
        if blank_row > 0:
            moves.append('up')
        if blank_row < 2:
            moves.append('down')
        if blank_col > 0:
            moves.append('left')
        if blank_col < 2:
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
        from collections import deque

        initial_state_tuple = tuple(tuple(row) for row in self.initial_state)
        goal_state_tuple = tuple(tuple(row) for row in self.goal_state)
        
        visited = {initial_state_tuple: None}  # Store state: parent state
        queue = deque([(self.initial_state, [])]) # Queue of (state, path)

        while queue:
            current_state, path = queue.popleft()
            current_state_tuple = tuple(tuple(row) for row in current_state)

            if current_state == self.goal_state:
                return path

            possible_moves = self.get_possible_moves(current_state)
            for move in possible_moves:
                new_state = self.move(current_state, move)

                if new_state:
                    new_state_tuple = tuple(tuple(row) for row in new_state)
                    if new_state_tuple not in visited:
                        visited[new_state_tuple] = current_state_tuple
                        queue.append((new_state, path + [move]))

        return None  # No solution found