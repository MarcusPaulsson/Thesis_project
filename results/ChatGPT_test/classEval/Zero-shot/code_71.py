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

        dr, dc = direction_map[direction]
        new_player_row = self.player_row + dr
        new_player_col = self.player_col + dc

        if self.map[new_player_row][new_player_col] == '#':
            return False  # Wall

        if self.map[new_player_row][new_player_col] == ' ':
            # Move player to empty space
            self.player_row, self.player_col = new_player_row, new_player_col
        elif self.map[new_player_row][new_player_col] == 'X':
            # Check if we can push the box
            box_new_row = new_player_row + dr
            box_new_col = new_player_col + dc

            if self.map[box_new_row][box_new_col] in [' ', 'G']:
                # Move the box
                self.boxes.remove((new_player_row, new_player_col))
                if self.map[box_new_row][box_new_col] == 'G':
                    self.boxes.append((box_new_row, box_new_col))
                else:
                    self.boxes.append((box_new_row, box_new_col))
                self.player_row, self.player_col = new_player_row, new_player_col

        return self.check_win()

    def print_map(self):
        """
        Print the current state of the map for debugging purposes.
        """
        for r in range(len(self.map)):
            line = list(self.map[r])
            if r == self.player_row:
                line[self.player_col] = 'O'
            for box in self.boxes:
                if box[0] == r:
                    line[box[1]] = 'X'
            print(''.join(line))