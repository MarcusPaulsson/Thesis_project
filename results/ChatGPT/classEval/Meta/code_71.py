class PushBoxGame:
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
        for row in range(len(self.map)):
            for col in range(len(self.map[row])):
                if self.map[row][col] == 'O':
                    self.player_row, self.player_col = row, col
                elif self.map[row][col] == 'G':
                    self.targets.append((row, col))
                elif self.map[row][col] == 'X':
                    self.boxes.append((row, col))
        self.target_count = len(self.targets)

    def check_win(self):
        self.is_game_over = all(box in self.targets for box in self.boxes)
        return self.is_game_over

    def move(self, direction):
        if self.is_game_over:
            return True

        direction_map = {
            'w': (-1, 0),  # up
            's': (1, 0),   # down
            'a': (0, -1),  # left
            'd': (0, 1)    # right
        }

        if direction not in direction_map:
            return False

        delta_row, delta_col = direction_map[direction]
        new_player_row = self.player_row + delta_row
        new_player_col = self.player_col + delta_col

        if self.map[new_player_row][new_player_col] == '#':
            return False  # hit a wall

        if (new_player_row, new_player_col) in self.boxes:
            new_box_row = new_player_row + delta_row
            new_box_col = new_player_col + delta_col

            if self.map[new_box_row][new_box_col] == '#' or (new_box_row, new_box_col) in self.boxes:
                return False  # can't move the box

            # Move the box
            box_index = self.boxes.index((new_player_row, new_player_col))
            self.boxes[box_index] = (new_box_row, new_box_col)

        # Move the player
        self.player_row = new_player_row
        self.player_col = new_player_col

        return self.check_win()

    def print_map(self):
        for row in range(len(self.map)):
            line = ''
            for col in range(len(self.map[row])):
                if (row, col) == (self.player_row, self.player_col):
                    line += 'O'
                elif (row, col) in self.boxes:
                    line += 'X'
                elif (row, col) in self.targets:
                    line += 'G'
                else:
                    line += self.map[row][col]
            print(line)