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
        for row in range(len(self.map)):
            for col in range(len(self.map[row])):
                if self.map[row][col] == 'O':
                    self.player_row = row
                    self.player_col = col
                elif self.map[row][col] == 'G':
                    self.targets.append((row, col))
                    self.target_count += 1
                elif self.map[row][col] == 'X':
                    self.boxes.append((row, col))

    def check_win(self):
        """
        Check if the game is won. The game is won when all the boxes are placed on target positions.
        And update the value of self.is_game_over.
        :return self.is_game_over: True if all the boxes are placed on target positions, or False otherwise.
        """
        for box in self.boxes:
            if box not in self.targets:
                return False
        self.is_game_over = True
        return True

    def move(self, direction):
        """
        Move the player based on the specified direction and check if the game is won.
        :param direction: str, the direction of the player's movement. 
            It can be 'w', 's', 'a', or 'd' representing up, down, left, or right respectively.

        :return: True if the game is won, False otherwise.
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
            return False

        if not (0 <= new_row < len(self.map) and 0 <= new_col < len(self.map[0]) and self.map[new_row][new_col] != '#'):
            return False

        # Check if moving into a box
        for i, box in enumerate(self.boxes):
            if box == (new_row, new_col):
                # Try to push the box
                push_row = new_row + (new_row - self.player_row)
                push_col = new_col + (new_col - self.player_col)

                if (0 <= push_row < len(self.map) and 0 <= push_col < len(self.map[0]) and
                        self.map[push_row][push_col] != '#'):
                    self.boxes[i] = (push_row, push_col)
                    self.player_row = new_row
                    self.player_col = new_col
                    return self.check_win()
                else:
                    return False
        else:
            # Move to the new position
            self.player_row = new_row
            self.player_col = new_col
            return self.check_win()