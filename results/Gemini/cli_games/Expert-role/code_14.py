import math
import random
import time

class AsteroidGame:
    """
    A command-line Asteroid game.
    """

    def __init__(self, width=80, height=20, asteroid_count=5, max_speed=1.0):
        """
        Initializes the game.

        Args:
            width (int): Width of the game board.
            height (int): Height of the game board.
            asteroid_count (int): Number of asteroids at the start.
            max_speed (float): Maximum speed of asteroids.
        """
        self.width = width
        self.height = height
        self.asteroid_count = asteroid_count
        self.max_speed = max_speed
        self.player_x = width // 2
        self.player_y = height // 2
        self.player_angle = 0  # Radians
        self.player_speed = 0
        self.asteroids = []
        self.bullets = []
        self.game_over = False
        self.score = 0
        self.lives = 3
        self.last_shot_time = 0  # To limit firing rate
        self.bullet_cooldown = 0.2  # Seconds between shots

        self.initialize_asteroids()

    def initialize_asteroids(self):
        """
        Creates the initial asteroids.
        """
        self.asteroids = []
        for _ in range(self.asteroid_count):
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(0.1, self.max_speed)
            self.asteroids.append({
                'x': x,
                'y': y,
                'angle': angle,
                'speed': speed,
                'size': 2  # Small size for now
            })

    def update(self, action):
        """
        Updates the game state based on player action.

        Args:
            action (str): Player action ('left', 'right', 'forward', 'fire', 'none').
        """
        if self.game_over:
            return

        # Player movement
        if action == 'left':
            self.player_angle -= 0.2
        elif action == 'right':
            self.player_angle += 0.2
        elif action == 'forward':
            self.player_speed = min(5, self.player_speed + 0.5) # Speed Limit

        # Decelerate
        self.player_speed = max(0, self.player_speed - 0.1)

        dx = self.player_speed * math.cos(self.player_angle)
        dy = self.player_speed * math.sin(self.player_angle)
        self.player_x = (self.player_x + dx) % self.width
        self.player_y = (self.player_y + dy) % self.height

        # Shooting
        current_time = time.time()
        if action == 'fire' and current_time - self.last_shot_time > self.bullet_cooldown:
            self.fire_bullet()
            self.last_shot_time = current_time
        
        # Update bullets
        self.update_bullets()

        # Update asteroids
        self.update_asteroids()

        # Check for collisions
        self.check_collisions()

    def fire_bullet(self):
        """
        Fires a bullet from the player's position.
        """
        bullet_speed = 8  # Bullet speed
        bullet_x = self.player_x
        bullet_y = self.player_y
        bullet_angle = self.player_angle
        self.bullets.append({
            'x': bullet_x,
            'y': bullet_y,
            'angle': bullet_angle,
            'speed': bullet_speed
        })

    def update_bullets(self):
        """
        Updates the position of all bullets and removes those that are out of bounds.
        """
        new_bullets = []
        for bullet in self.bullets:
            dx = bullet['speed'] * math.cos(bullet['angle'])
            dy = bullet['speed'] * math.sin(bullet['angle'])
            bullet['x'] = (bullet['x'] + dx) % self.width
            bullet['y'] = (bullet['y'] + dy) % self.height

            # Keep bullets if within bounds
            if 0 <= bullet['x'] < self.width and 0 <= bullet['y'] < self.height:
                new_bullets.append(bullet)

        self.bullets = new_bullets

    def update_asteroids(self):
        """
        Updates the position of all asteroids.
        """
        for asteroid in self.asteroids:
            dx = asteroid['speed'] * math.cos(asteroid['angle'])
            dy = asteroid['speed'] * math.sin(asteroid['angle'])
            asteroid['x'] = (asteroid['x'] + dx) % self.width
            asteroid['y'] = (asteroid['y'] + dy) % self.height

    def check_collisions(self):
        """
        Checks for collisions between player, asteroids, and bullets.
        """
        # Player-Asteroid collision
        for asteroid in self.asteroids:
            distance = math.sqrt((self.player_x - asteroid['x'])**2 + (self.player_y - asteroid['y'])**2)
            if distance < asteroid['size'] + 1:  # Collision radius
                self.lives -= 1
                self.player_x = self.width // 2
                self.player_y = self.height // 2
                self.player_speed = 0
                self.initialize_asteroids()  # Reset Asteroids
                if self.lives <= 0:
                    self.game_over = True
                return  # Only lose one life per frame

        # Bullet-Asteroid collision
        new_asteroids = []
        new_bullets = []
        for asteroid in self.asteroids:
            hit = False
            for bullet in self.bullets:
                distance = math.sqrt((bullet['x'] - asteroid['x'])**2 + (bullet['y'] - asteroid['y'])**2)
                if distance < asteroid['size']:
                    self.score += 10
                    hit = True
                    break  # One bullet can only hit one asteroid
            if not hit:
                new_asteroids.append(asteroid)
            else:
                # Split asteroid (simple version - just remove)
                pass

            if not hit:
                new_asteroids.append(asteroid)

        for bullet in self.bullets:
            hit = False
            for asteroid in self.asteroids:
                distance = math.sqrt((bullet['x'] - asteroid['x'])**2 + (bullet['y'] - asteroid['y'])**2)
                if distance < asteroid['size']:
                    hit = True
                    break
            if not hit:
                new_bullets.append(bullet)

        self.asteroids = new_asteroids
        self.bullets = new_bullets

        if not self.asteroids:
            self.asteroid_count += 2 # Increased Difficulty
            self.initialize_asteroids()

    def draw(self):
        """
        Draws the game state to the console.

        Returns:
            str: A string representation of the game board.
        """
        board = [[' ' for _ in range(self.width)] for _ in range(self.height)]

        # Draw player (triangle for simplicity)
        player_x = int(round(self.player_x))
        player_y = int(round(self.player_y))
        if 0 <= player_x < self.width and 0 <= player_y < self.height:
           board[player_y][player_x] = '^'

        # Draw asteroids
        for asteroid in self.asteroids:
            x = int(round(asteroid['x']))
            y = int(round(asteroid['y']))
            if 0 <= x < self.width and 0 <= y < self.height:
                board[y][x] = 'O'

        # Draw bullets
        for bullet in self.bullets:
            x = int(round(bullet['x']))
            y = int(round(bullet['y']))
            if 0 <= x < self.width and 0 <= y < self.height:
                board[y][x] = '.'

        # Convert board to string
        output = ""
        for row in board:
            output += ''.join(row) + '\n'

        # Add score and lives
        output += f"Score: {self.score}  Lives: {self.lives}\n"

        if self.game_over:
            output = "Game Over!\n" + output

        return output

    def play(self):
        """
        Runs the main game loop.
        """
        while not self.game_over:
            print(self.draw())
            action = input("Action (left, right, forward, fire, none): ").lower()
            self.update(action)
            time.sleep(0.05)  # Control game speed

        print(self.draw())
        print("Final Score:", self.score)

if __name__ == '__main__':
    game = AsteroidGame()
    game.play()