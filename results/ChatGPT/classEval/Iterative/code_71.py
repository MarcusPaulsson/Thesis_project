class PushBoxGame:
    """
    This class implements a functionality of a sokoban game, where the player needs to move boxes to designated targets in order to win.
    """

    def __init__(self, game_map):
        """
        Initialize the push box game with the map and various attributes.
        :param game_map: list[str], the map of the push box game, represented as a list of strings. 
            Each character on the map represents a different element, including the following:
            - '#' represents a wall that neither the player nor the box can pass through;
            - 'O' represents the initial position of the player;
            - 'G' represents the target position;
            - 'X' represents the initial position of the box.
        >>> map = ["#####", "#O  #", "# X #", "#  G#", "#####"]   
        >>> game = PushBoxGame(map)                
        """
        self.map = game_map
        self.player_row, self.player_col = self._find_player()
        self.targets = self._find_targets()
        self.boxes = self._find_boxes()
        self.target_count = len(self.targets)
        self.is_game_over = False

    def _find_player(self):
        for r, row in enumerate(self.map):
            for c, char in enumerate(row):
                if char == 'O':
                    return r, c
        return None, None

    def _find_targets(self):
        return [(r, c) for r, row in enumerate(self.map) for c, char in enumerate(row) if char == 'G']

    def _find_boxes(self):
        return [(r, c) for r, row in enumerate(self.map) for c, char in enumerate(row) if char == 'X']

    def check_win(self):
        """
        Check if the game is won. The game is won when all the boxes are placed on target positions.
        And update the value of self.is_game_over.
        :return: True if all the boxes are placed on target positions, or False otherwise.
        >>> game = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"]) 
        >>> game.check_win()
        False
        """
        self.is_game_over = all(box in self.targets for box in self.boxes)
        return self.is_game_over

    def move(self, direction):
        """
        Move the player based on the specified direction and check if the game is won.
        :param direction: str, the direction of the player's movement. 
            It can be 'w', 's', 'a', or 'd' representing up, down, left, or right respectively.

        :return: True if the game is won, False otherwise.
        >>> game = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"])       
        >>> game.print_map()
        # # # # # 
        # O     #
        #   X   #
        #     G #
        # # # # #
        >>> game.move('d')
        False
        >>> game.move('s')   
        False
        >>> game.move('a')   
        False
        >>> game.move('s') 
        False
        >>> game.move('d') 
        True
        """
        moves = {
            'w': (-1, 0),
            's': (1, 0),
            'a': (0, -1),
            'd': (0, 1)
        }

        if direction in moves:
            dr, dc = moves[direction]
            new_player_row = self.player_row + dr
            new_player_col = self.player_col + dc
            
            if self._is_valid_move(new_player_row, new_player_col):
                if (new_player_row, new_player_col) in self.boxes:
                    new_box_row = new_player_row + dr
                    new_box_col = new_player_col + dc
                    if self._is_valid_move(new_box_row, new_box_col) and (new_box_row, new_box_col) not in self.boxes:
                        self.boxes.remove((new_player_row, new_player_col))
                        self.boxes.append((new_box_row, new_box_col))
                self.player_row, self.player_col = new_player_row, new_player_col

        return self.check_win()

    def _is_valid_move(self, row, col):
        return 0 <= row < len(self.map) and 0 <= col < len(self.map[0]) and self.map[row][col] != '#'

    def print_map(self):
        for r in range(len(self.map)):
            row = list(self.map[r])
            if (r, self.player_col) == (self.player_row, self.player_col):
                row[self.player_col] = 'O'
            for box in self.boxes:
                if box[0] == r:
                    row[box[1]] = 'X'
            print("".join(row))