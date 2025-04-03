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
        for row in range(len(self.map)):
            for col in range(len(self.map[row])):
                if self.map[row][col] == 'O':
                    self.player_row, self.player_col = row, col
                elif self.map[row][col] == 'G':
                    self.targets.append((row, col))
                    self.target_count += 1
                elif self.map[row][col] == 'X':
                    self.boxes.append((row, col))

    def check_win(self):
        self.is_game_over = all(box in self.targets for box in self.boxes)
        return self.is_game_over

    def move(self, direction):
        if self.is_game_over:
            return True
        
        delta = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}
        if direction in delta:
            d_row, d_col = delta[direction]
            new_row = self.player_row + d_row
            new_col = self.player_col + d_col
            
            if self.map[new_row][new_col] == '#':
                return False
            
            if (new_row, new_col) in self.boxes:
                box_new_row = new_row + d_row
                box_new_col = new_col + d_col
                
                if self.map[box_new_row][box_new_col] == '#' or (box_new_row, box_new_col) in self.boxes:
                    return False
                
                # Move the box
                self.boxes.remove((new_row, new_col))
                self.boxes.append((box_new_row, box_new_col))
                
            # Move the player
            self.player_row = new_row
            self.player_col = new_col
            
            return self.check_win()

    def print_map(self):
        visual_map = [list(row) for row in self.map]
        visual_map[self.player_row][self.player_col] = 'O'
        for box in self.boxes:
            visual_map[box[0]][box[1]] = 'X'
        for target in self.targets:
            visual_map[target[0]][target[1]] = 'G'
        
        for row in visual_map:
            print(''.join(row))