import random

class MahjongConnect:
    def __init__(self, BOARD_SIZE, ICONS):
        self.BOARD_SIZE = BOARD_SIZE
        self.ICONS = ICONS
        self.board = self.create_board()

    def create_board(self):
        rows, cols = self.BOARD_SIZE
        icons = self.ICONS * ((rows * cols) // len(self.ICONS))
        icons = icons[:rows * cols]
        random.shuffle(icons)
        board = [icons[i * cols:(i + 1) * cols] for i in range(rows)]
        return board

    def is_valid_move(self, pos1, pos2):
        if pos1 == pos2:
            return False
        if not self.is_within_bounds(pos1) or not self.is_within_bounds(pos2):
            return False
        if self.board[pos1[0]][pos1[1]] != self.board[pos2[0]][pos2[1]]:
            return False
        return self.has_path(pos1, pos2)

    def is_within_bounds(self, pos):
        x, y = pos
        return 0 <= x < self.BOARD_SIZE[0] and 0 <= y < self.BOARD_SIZE[1]

    def has_path(self, pos1, pos2):
        # Path finding logic here (for simplicity, assume there is always a path for valid moves)
        return True

    def remove_icons(self, pos1, pos2):
        self.board[pos1[0]][pos1[1]] = ' '
        self.board[pos2[0]][pos2[1]] = ' '

    def is_game_over(self):
        return all(icon == ' ' for row in self.board for icon in row)