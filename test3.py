import gamepad
from gamepad import Game

class BattleshipGame(Game):
    def __init__(self):
        super().__init__()
        
        # Initialize the board
        self.board = []
        for row in range(10):
            self.board.append([''] * 10)
        
        # Place ships
        selfships = {
            'water': [[False for _ in range(10)] for _ in range(10)],
            'ship_a': [[True for _ in range(5)] for _ in range(5)],
            'ship_b': [[True for _ in range(4)] for _ in range(4)],
            'ship_c': [[True for _ in range(3)] for _ in range(3)],
            'ship_d': [[True for _ in range(2)] for _ in range(2)],
            'ship_e': [[True for _ in range(1)] for _ in range(1)]
        }
        
        # Place each ship randomly on separate rows and columns
        for ship, pos in selfships.items():
            while True:
                try:
                    row, col = random.randint(0,9), random.randint(0,9)
                    if not pos[row][col]:
                        break
                except StopIteration:
                    pass
        
        self.board[ship].update(pos)
        
        # Keep track of hit hits
        self.hits = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}
        
        # Keep track of remaining shots
        self.shots_left = {}
        for ship, pos in selfships.items():
            count = 0
            while True:
                try:
                    row, col = random.randint(0,9), random.randint(0,9)
                    if not pos[row][col] or self.board[ship][row][col]:
                        break
                    count += 1
                except StopIteration:
                    break
            self.shots_left[ship] = count - (count // 5)  # Subtract 5% for sunk
    
    def update(self, data=None):
        "Update the game state."
        if data is None:
            return
            
        # Update the board
        self.board = [list(row) for row in data]
        
        # Update hit status
        for ship, pos in selfships.items():
            hit = False
            for row in range(10):
                for col in range(10):
                    if pos[row][col] and self.board[ship][row][col]:
                        self.hits[ship] = max(self.hits[ship], 1)
                        hit = True
                        break
                if hit:
                    break
        
        # Check for sunk ships
        for ship, pos in selfships.items():
            sunk = False
            for row in range(10):
                for col in range(10):
                    if pos[row][col] and self.board[ship][row][col]:
                        self.hits[ship] += 1
                        sunk = True
                        break
                if sunk:
                    break
                if self.board[ship][row][col]:  # Ship is still there but missed a hit
                    continue
                else:
                    self.shots_left[ship] -= 1
                    if self.shots_left[ship] == 0:
                        self.game_over()
        
        # Draw the board
        self.draw_board()
    
    def draw_board(self):
        "Draw the current game board."
        for row in range(10):
            row_str = ""
            for col in range(10):
                if self.board[row][col]:
                    row_str += "|X"
                else:
                    row_str += "| "
            print(f" {row_str}")
            
    def get_keypress(self, key):
        "Handle keyboard input for clicks."
        return key
    
    def game_over(self):
        "End the game when user presses space."
        print("Game Over!")
        sys.exit(0)
        
    def main(self):
        "Main entry point for the game."
        self.board = [[False for _ in range(10)] for _ in range(10)]
        self.update()
        
        while True:
            self.main()
            
            # Get input from left mouse button
            x, y = self.get_keypress('l')
            
            # Get input from right mouse button
            if y > 0:
                x, y = self.get_keypress('r')
                
            # Check for win condition
            if x == 10 and y == 10:
                self.game_over()
                break
                
            # Check for sunk ships
            for ship, pos in selfships.items():
                sunk = False
                for row in range(10):
                    for col in range(10):
                        if pos[row][col] and self.board[ship][row][col]:
                            self.hits[ship] += 1
                            sunk = True
                            break
                    if sunk:
                        break
                if sunk:
                    continue
                    
                # Check if all hits are used
                if self.hits[ship] == len(self.shots_left[ship]):
                    self.game_over()
                    break
                
            # Check for shoot limit
            total_shots = sum(self.shotshits_left.values())
            if total_shots <= 0:
                self.game_over()
                break
            
            # Update the board and hits
            self.board = [[False for _ in range(10)] for _ in range(10)]
            self.update()
            
            # Wait for user to press enter or click outside
            self.wait()

if __name__ == "__main__":
    app = BattleshipGame()
    app.main()