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
        for row_index, row in enumerate(self.map):
            for col_index, cell in enumerate(row):
                if cell == 'O':
                    self.player_row = row_index
                    self.player_col = col_index
                elif cell == 'G':
                    self.targets.append((row_index, col_index))
                    self.target_count += 1
                elif cell == 'X':
                    self.boxes.append((row_index, col_index))

    def check_win(self):
        """
        Check if the game is won. The game is won when all the boxes are placed on target positions.
        And update the value of self.is_game_over.
        :return self.is_game_over: True if all the boxes are placed on target positions, or False otherwise.
        >>> game = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"]) 
        >>> game.check_win()
        """
        for box in self.boxes:
            if box not in self.targets:
                self.is_game_over = False
                return self.is_game_over
        self.is_game_over = True
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
        new_row = self.player_row
        new_col = self.player_col

        if direction == 'w':
            new_row -= 1
        elif direction == 's':
            new_row += 1
        elif direction == 'a':
            new_col -= 1
        elif direction == 'd':
            new_col += 1
        else:
            return self.check_win()

        if not (0 <= new_row < len(self.map) and 0 <= new_col < len(self.map[0])):
            return self.check_win()

        if self.map[new_row][new_col] == '#':
            return self.check_win()

        box_index = -1
        for i, box in enumerate(self.boxes):
            if box[0] == new_row and box[1] == new_col:
                box_index = i
                break

        if box_index != -1:
            box_new_row = new_row + (new_row - self.player_row)
            box_new_col = new_col + (new_col - self.player_col)

            if not (0 <= box_new_row < len(self.map) and 0 <= box_new_col < len(self.map[0])):
                return self.check_win()

            if self.map[box_new_row][box_new_col] == '#':
                return self.check_win()

            box_collision = False
            for other_box in self.boxes:
                if other_box[0] == box_new_row and other_box[1] == box_new_col:
                    box_collision = True
                    break
            
            if box_collision:
                return self.check_win()

            self.boxes[box_index] = (box_new_row, box_new_col)
            self.player_row = new_row
            self.player_col = new_col
        else:
            self.player_row = new_row
            self.player_col = new_col

        return self.check_win()

    def print_map(self):
        """
        Print the current map of the game.
        """
        for row in self.map:
            print(' '.join(row))