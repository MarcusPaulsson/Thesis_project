class EightPuzzle:
    """
    This class is an implementation of the classic 8-puzzle game, including methods for finding the blank tile, making moves, getting possible moves, and solving the puzzle using a breadth-first search algorithm.
    """

    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def find_blank(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return (i, j)
        return None

    def move(self, state, direction):
        blank_i, blank_j = self.find_blank(state)
        new_state = [row[:] for row in state]

        if direction == 'up' and blank_i > 0:
            new_state[blank_i][blank_j], new_state[blank_i - 1][blank_j] = new_state[blank_i - 1][blank_j], new_state[blank_i][blank_j]
        elif direction == 'down' and blank_i < 2:
            new_state[blank_i][blank_j], new_state[blank_i + 1][blank_j] = new_state[blank_i + 1][blank_j], new_state[blank_i][blank_j]
        elif direction == 'left' and blank_j > 0:
            new_state[blank_i][blank_j], new_state[blank_i][blank_j - 1] = new_state[blank_i][blank_j - 1], new_state[blank_i][blank_j]
        elif direction == 'right' and blank_j < 2:
            new_state[blank_i][blank_j], new_state[blank_i][blank_j + 1] = new_state[blank_i][blank_j + 1], new_state[blank_i][blank_j]
        else:
            return state  # Invalid move

        return new_state

    def get_possible_moves(self, state):
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
        from collections import deque

        open_list = deque([(self.initial_state, [])])
        visited = set()
        visited.add(tuple(map(tuple, self.initial_state)))

        while open_list:
            current_state, path = open_list.popleft()

            if current_state == self.goal_state:
                return path

            for move_direction in self.get_possible_moves(current_state):
                new_state = self.move(current_state, move_direction)
                if tuple(map(tuple, new_state)) not in visited:
                    visited.add(tuple(map(tuple, new_state)))
                    open_list.append((new_state, path + [move_direction]))

        return None