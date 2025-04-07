class PushBoxGame:
    """
    This class implements a functionality of a sokoban game, where the player needs to move boxes to designated targets in order to win.
    """

    def __init__(self, map):
        self.map = map
        self.player_row = 0
        self.player_col = 0
        self.targets = []
        self.boxes = []
        self.target_count = 0
        self.is_game_over = False
        self.init_game()

    def init_game(self):
        for r in range(len(self.map)):
            for c in range(len(self.map[r])):
                if self.map[r][c] == 'O':
                    self.player_row, self.player_col = r, c
                elif self.map[r][c] == 'G':
                    self.targets.append((r, c))
                elif self.map[r][c] == 'X':
                    self.boxes.append((r, c))
        self.target_count = len(self.targets)

    def check_win(self):
        self.is_game_over = all(box in self.targets for box in self.boxes)
        return self.is_game_over

    def move(self, direction):
        if self.is_game_over:
            return True

        move_directions = {
            'w': (-1, 0),
            's': (1, 0),
            'a': (0, -1),
            'd': (0, 1)
        }

        if direction in move_directions:
            dr, dc = move_directions[direction]
            new_player_row = self.player_row + dr
            new_player_col = self.player_col + dc

            if self.map[new_player_row][new_player_col] != '#':
                if (new_player_row, new_player_col) in self.boxes:
                    new_box_row = new_player_row + dr
                    new_box_col = new_player_col + dc
                    if self.map[new_box_row][new_box_col] != '#' and (new_box_row, new_box_col) not in self.boxes:
                        self.boxes.remove((new_player_row, new_player_col))
                        self.boxes.append((new_box_row, new_box_col))
                self.player_row, self.player_col = new_player_row, new_player_col

        return self.check_win()

    def print_map(self):
        for r in range(len(self.map)):
            row = list(self.map[r])
            if r == self.player_row:
                row[self.player_col] = 'O'
            for box in self.boxes:
                if box[0] == r:
                    row[box[1]] = 'X'
            print("".join(row))