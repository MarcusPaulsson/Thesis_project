class PushBoxGame:
    """
    This class implements a functionality of a sokoban game, where the player needs to move boxes to designated targets in order to win.
    """

    def __init__(self, map):
        """
        Initialize the push box game with the map and various attributes.
        :param map: list[str], the map of the push box game, represented as a list of strings. 
            Each character on the map represents a different element, including the following:
            - '#' represents a wall that neither the player nor the box can pass through;
            - 'O' represents the initial position of the player;
            - 'G' represents the target position;
            - 'X' represents the initial position of the box.
        >>> map = ["#####", "#O  #", "# X #", "#  G#", "#####"]   
        >>> game = PushBoxGame(map)                
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
        >>> game = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"]) 
        >>> game.targets
        [(3, 3)]
        >>> game.boxes
        [(2, 2)]
        >>> game.player_row
        1
        >>> game.player_col
        1
        """
        for r, line in enumerate(self.map):
            for c, char in enumerate(line):
                if char == 'O':
                    self.player_row, self.player_col = r, c
                elif char == 'G':
                    self.targets.append((r, c))
                    self.target_count += 1
                elif char == 'X':
                    self.boxes.append((r, c))

    def check_win(self):
        """
        Check if the game is won. The game is won when all the boxes are placed on target positions.
        And update the value of self.is_game_over.
        :return self.is_game_over: True if all the boxes are placed on target positions, or False otherwise.
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
        direction_map = {
            'w': (-1, 0),
            's': (1, 0),
            'a': (0, -1),
            'd': (0, 1)
        }
        
        if direction not in direction_map:
            return False
        
        d_row, d_col = direction_map[direction]
        new_player_row = self.player_row + d_row
        new_player_col = self.player_col + d_col

        if self.map[new_player_row][new_player_col] == '#':
            return False  # Wall collision

        if (new_player_row, new_player_col) in self.boxes:
            new_box_row = new_player_row + d_row
            new_box_col = new_player_col + d_col
            
            if self.map[new_box_row][new_box_col] == '#' or (new_box_row, new_box_col) in self.boxes:
                return False  # Wall or box collision
            
            # Move the box
            box_index = self.boxes.index((new_player_row, new_player_col))
            self.boxes[box_index] = (new_box_row, new_box_col)

        # Move the player
        self.player_row, self.player_col = new_player_row, new_player_col
        
        return self.check_win()

    def print_map(self):
        """
        Prints the current state of the game map.
        """
        for r in range(len(self.map)):
            row = list(self.map[r])
            if (r, self.player_col) == (self.player_row, self.player_col):
                row[self.player_col] = 'O'
            for box in self.boxes:
                if box[0] == r:
                    row[box[1]] = 'X'
            print(''.join(row))