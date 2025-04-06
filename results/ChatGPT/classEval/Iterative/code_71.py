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
        """
        self.map = game_map
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
        for r, row in enumerate(self.map):
            for c, char in enumerate(row):
                if char == 'O':
                    self.player_row, self.player_col = r, c
                elif char == 'G':
                    self.targets.append((r, c))
                elif char == 'X':
                    self.boxes.append((r, c))

    def check_win(self):
        """
        Check if the game is won. The game is won when all the boxes are placed on target positions.
        And update the value of self.is_game_over.
        :return: True if all the boxes are placed on target positions, or False otherwise.
        """
        self.is_game_over = all(box in self.targets for box in self.boxes)
        return self.is_game_over

    def move(self, direction):
        """
        Move the player based on the specified direction and check if the game is won.
        :param direction: str, the direction of the player's movement.
            It can be 'w', 's', 'a', or 'd' representing up, down, left, or right respectively.
        :return: True if the game is won, False otherwise.
        """
        directions = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}
        if direction not in directions:
            return False

        dr, dc = directions[direction]
        new_player_row = self.player_row + dr
        new_player_col = self.player_col + dc

        # Check for walls or out of bounds
        if (0 <= new_player_row < len(self.map) and 
            0 <= new_player_col < len(self.map[0]) and 
            self.map[new_player_row][new_player_col] != '#'):
            if (new_player_row, new_player_col) in self.boxes:
                new_box_row = new_player_row + dr
                new_box_col = new_player_col + dc
                if (0 <= new_box_row < len(self.map) and 
                    0 <= new_box_col < len(self.map[0]) and 
                    self.map[new_box_row][new_box_col] != '#' and 
                    (new_box_row, new_box_col) not in self.boxes):
                    # Move the box
                    box_index = self.boxes.index((new_player_row, new_player_col))
                    self.boxes[box_index] = (new_box_row, new_box_col)
                else:
                    return False  # Wall or another box in the way
            # Move the player
            self.player_row = new_player_row
            self.player_col = new_player_col

            # Check if the game is won
            return self.check_win()
        return False  # Wall or out of bounds

    def print_map(self):
        """
        Print the current state of the map.
        """
        display_map = []
        for r in range(len(self.map)):
            row = list(self.map[r])
            if (r, self.player_col) == (self.player_row, self.player_col):
                row[self.player_col] = 'O'
            for box in self.boxes:
                if (r, box[1]) == box:
                    row[box[1]] = 'X'
            display_map.append(''.join(row))
        print('\n'.join(display_map))