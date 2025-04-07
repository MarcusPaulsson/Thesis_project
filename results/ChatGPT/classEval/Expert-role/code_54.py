import random

class MahjongConnect:
    def __init__(self, BOARD_SIZE, ICONS):
        self.BOARD_SIZE = BOARD_SIZE
        self.ICONS = ICONS
        self.board = self.create_board()

    def create_board(self):
        icons_count = self.BOARD_SIZE[0] * self.BOARD_SIZE[1] // 2
        icons = (self.ICONS * (icons_count // len(self.ICONS))) + random.sample(self.ICONS, icons_count % len(self.ICONS))
        random.shuffle(icons)
        board = [icons[i:i + self.BOARD_SIZE[1]] for i in range(0, len(icons), self.BOARD_SIZE[1])]
        return board

    def is_valid_move(self, pos1, pos2):
        if pos1 == pos2:
            return False
        if not (0 <= pos1[0] < self.BOARD_SIZE[0] and 0 <= pos1[1] < self.BOARD_SIZE[1]) or not (0 <= pos2[0] < self.BOARD_SIZE[0] and 0 <= pos2[1] < self.BOARD_SIZE[1]):
            return False
        if self.board[pos1[0]][pos1[1]] != self.board[pos2[0]][pos2[1]]:
            return False
        return self.has_path(pos1, pos2)

    def has_path(self, pos1, pos2):
        if pos1 == pos2:
            return True
        return self._has_path(pos1, pos2, set())

    def _has_path(self, pos1, pos2, visited):
        if pos1 == pos2:
            return True
        if pos1 in visited:
            return False
        visited.add(pos1)

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in directions:
            for step in range(1, max(self.BOARD_SIZE)):
                x, y = pos1[0] + dx * step, pos1[1] + dy * step
                if 0 <= x < self.BOARD_SIZE[0] and 0 <= y < self.BOARD_SIZE[1]:
                    if self.board[x][y] == ' ':
                        if self._has_path((x, y), pos2, visited):
                            return True
                    elif (x, y) == pos2:
                        return True
                else:
                    break
        return False

    def remove_icons(self, pos1, pos2):
        if self.is_valid_move(pos1, pos2):
            self.board[pos1[0]][pos1[1]] = ' '
            self.board[pos2[0]][pos2[1]] = ' '

    def is_game_over(self):
        for row in self.board:
            for icon in row:
                if icon != ' ':
                    return False
        return True