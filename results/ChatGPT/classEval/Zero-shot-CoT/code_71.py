class PushBoxGame:
    """
    This class implements a functionality of a sokoban game, where the player needs to move boxes to designated targets in order to win.
    """

    def __init__(self, map):
        """
        Initialize the push box game with the map and various attributes.
        :param map: list[str], the map of the push box game, represented as a list of strings.
        """
        self.map = map
        self.player_row = 0
        self.player_col = 0
        self.targets = []
        self.boxes = []
        self.target_count = 0
        self.is_game_over = False
        self.init_game()

    def init_game(self):
        """
        Initialize the game by setting the positions of the player, targets, and boxes based on the map.
        """
        for i, row in enumerate(self.map):
            for j, char in enumerate(row):
                if char == 'O':
                    self.player_row, self.player_col = i, j
                elif char == 'G':
                    self.targets.append((i, j))
                elif char == 'X':
                    self.boxes.append((i, j))
        self.target_count = len(self.targets)

    def check_win(self):
        """
        Check if the game is won. The game is won when all the boxes are placed on target positions.
        And update the value of self.is_game_over.
        :return self.is_game_over: True if all the boxes are placed on target positions, or False otherwise.
        """
        self.is_game_over = all(box in self.targets for box in self.boxes)
        return self.is_game_over

    def move(self, direction):
        """
        Move the player based on the specified direction and check if the game is won.
        :param direction: str, the direction of the player's movement. 
        :return: True if the game is won, False otherwise.
        """
        move_offsets = {
            'w': (-1, 0),  # Up
            's': (1, 0),   # Down
            'a': (0, -1),  # Left
            'd': (0, 1)    # Right
        }
        
        if direction not in move_offsets:
            return False

        new_player_row = self.player_row + move_offsets[direction][0]
        new_player_col = self.player_col + move_offsets[direction][1]

        if self.map[new_player_row][new_player_col] == '#':
            return False  # Hit a wall

        if (new_player_row, new_player_col) in self.boxes:
            new_box_row = new_player_row + move_offsets[direction][0]
            new_box_col = new_player_col + move_offsets[direction][1]

            if self.map[new_box_row][new_box_col] == '#' or (new_box_row, new_box_col) in self.boxes:
                return False  # Hit a wall or another box
            
            # Move the box
            box_index = self.boxes.index((new_player_row, new_player_col))
            self.boxes[box_index] = (new_box_row, new_box_col)

        # Move the player
        self.player_row, self.player_col = new_player_row, new_player_col
        
        return self.check_win()

    def print_map(self):
        """
        Print the current state of the game map with player and boxes.
        """
        for i in range(len(self.map)):
            row = list(self.map[i])
            if (i, self.player_col) == (self.player_row, self.player_col):
                row[self.player_col] = 'O'
            for box in self.boxes:
                if box == (i, self.player_col):
                    row[box[1]] = 'X'
            print(''.join(row))