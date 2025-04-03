import random

class MahjongConnect:
    """
    MahjongConnect is a class representing a game board for Mahjong Connect with features like creating the board, checking valid moves, finding paths, removing icons, and checking if the game is over.
    """

    def __init__(self, BOARD_SIZE, ICONS):
        self.BOARD_SIZE = BOARD_SIZE
        self.ICONS = ICONS
        self.board = self.create_board()

    def create_board(self):
        num_icons = len(self.ICONS)
        total_cells = self.BOARD_SIZE[0] * self.BOARD_SIZE[1]
        icons_list = (self.ICONS * (total_cells // num_icons + 1))[:total_cells]
        random.shuffle(icons_list)
        return [icons_list[i:i + self.BOARD_SIZE[1]] for i in range(0, total_cells, self.BOARD_SIZE[1])]

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
        # Implement BFS or DFS to find a path; this is a simplified version
        return True  # Placeholder for path finding logic

    def remove_icons(self, pos1, pos2):
        self.board[pos1[0]][pos1[1]] = ' '
        self.board[pos2[0]][pos2[1]] = ' '

    def is_game_over(self):
        return all(cell == ' ' for row in self.board for cell in row)