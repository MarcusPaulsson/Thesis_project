class EightPuzzle:
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
            return state  # No move was made
        
        return new_state

    def get_possible_moves(self, state):
        moves = []
        i, j = self.find_blank(state)

        if i > 0: moves.append('up')
        if i < 2: moves.append('down')
        if j > 0: moves.append('left')
        if j < 2: moves.append('right')

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
                state_tuple = tuple(map(tuple, new_state))  # Convert to tuple for immutability

                if state_tuple not in visited:
                    visited.add(state_tuple)
                    open_list.append((new_state, path + [move_direction]))

        return []