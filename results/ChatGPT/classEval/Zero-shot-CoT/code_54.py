import random

class MahjongConnect:
    def __init__(self, BOARD_SIZE, ICONS):
        self.BOARD_SIZE = BOARD_SIZE
        self.ICONS = ICONS
        self.board = self.create_board()

    def create_board(self):
        rows, cols = self.BOARD_SIZE
        num_icons = (rows * cols) // 2
        icons = random.sample(self.ICONS, num_icons) * 2  # Duplicate icons
        random.shuffle(icons)  # Shuffle icons to place them randomly
        return [icons[i * cols:(i + 1) * cols] for i in range(rows)]

    def is_valid_move(self, pos1, pos2):
        if pos1 == pos2:
            return False
        if not (0 <= pos1[0] < self.BOARD_SIZE[0] and 0 <= pos1[1] < self.BOARD_SIZE[1]):
            return False
        if not (0 <= pos2[0] < self.BOARD_SIZE[0] and 0 <= pos2[1] < self.BOARD_SIZE[1]):
            return False
        if self.board[pos1[0]][pos1[1]] != self.board[pos2[0]][pos2[1]]:
            return False
        return self.has_path(pos1, pos2)

    def has_path(self, pos1, pos2):
        # Implement a simple DFS or BFS to check for a path
        if pos1 == pos2:
            return True
        
        visited = set()
        stack = [pos1]

        while stack:
            current = stack.pop()
            if current == pos2:
                return True
            if current in visited:
                continue
            visited.add(current)
            
            for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                next_pos = (current[0] + direction[0], current[1] + direction[1])
                if (0 <= next_pos[0] < self.BOARD_SIZE[0] and
                        0 <= next_pos[1] < self.BOARD_SIZE[1] and
                        self.board[next_pos[0]][next_pos[1]] == self.board[current[0]][current[1]]):
                    stack.append(next_pos)

        return False

    def remove_icons(self, pos1, pos2):
        self.board[pos1[0]][pos1[1]] = ' '
        self.board[pos2[0]][pos2[1]] = ' '

    def is_game_over(self):
        for row in self.board:
            for icon in row:
                if icon != ' ':
                    return False
        return True