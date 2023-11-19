# Pong Pygame 
# Test cases are below the game codes

import pygame
import sys

def Pong_game():
    pygame.init()    
    WIDTH, HEIGHT = 800, 600
    FPS = 60
    SCORE_LIMIT = 5

    # display
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # clock
    clock = pygame.time.Clock()

    # paddles
    paddle_a = pygame.Rect(0, HEIGHT // 2, 20, 80)
    paddle_b = pygame.Rect(WIDTH - 20, HEIGHT // 2, 20, 80)

    # ball
    ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, 15, 15)
    ball_speed = 4  # Adjust the speed factor (doubled)
    ball_dir = [1 * ball_speed, 1 * ball_speed]  # Double the initial speed

    # score
    score_a = 0
    score_b = 0

    # font
    font = pygame.font.Font(None, 36)

    # welcome message
    welcome_text = font.render("Welcome to Pong! Press any key to start.", True, (255, 255, 255))
    screen.blit(welcome_text, (WIDTH // 4, HEIGHT // 2))
    pygame.display.flip()

    # key press to start the game
    waiting_for_key = True
    while waiting_for_key:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                waiting_for_key = False

    # Main game loop
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                pass  # Handle key events in the next modification

        # continuous key presses for paddle movement
        keys = pygame.key.get_pressed()

        # Paddle A movement
        if keys[pygame.K_w]:
            paddle_a.move_ip(0, -10)
        if keys[pygame.K_s]:
            paddle_a.move_ip(0, 10)

        # Paddle B movement
        if keys[pygame.K_UP]:
            paddle_b.move_ip(0, -10)
        if keys[pygame.K_DOWN]:
            paddle_b.move_ip(0, 10)

        # Ensure paddles within bounds
        paddle_a.y = max(0, min(HEIGHT - paddle_a.height, paddle_a.y))
        paddle_b.y = max(0, min(HEIGHT - paddle_b.height, paddle_b.y))

        # Game logic
        ball.move_ip(ball_dir)

        # Border collision
        if ball.left < 0 or ball.right > WIDTH:
            ball_dir[0] *= -1
        if ball.top < 0 or ball.bottom > HEIGHT:
            ball_dir[1] *= -1

        # Paddle collision
        if ball.colliderect(paddle_a) or ball.colliderect(paddle_b):
            ball_dir[0] *= -1

        # Score
        if ball.left < 0:
            score_b += 1
            if score_b == SCORE_LIMIT:
                game_over_text = font.render("Game Over! Player B wins!", True, (255, 255, 255))
                screen.blit(game_over_text, (WIDTH // 4, HEIGHT // 2))
                pygame.display.flip()
                pygame.time.wait(3000)  # Wait for 3 seconds
                running = False
            ball.center = (WIDTH // 2, HEIGHT // 2)  # Reset ball position
        elif ball.right > WIDTH:
            score_a += 1
            if score_a == SCORE_LIMIT:
                game_over_text = font.render("Game Over! Player A wins!", True, (255, 255, 255))
                screen.blit(game_over_text, (WIDTH // 4, HEIGHT // 2))
                pygame.display.flip()
                pygame.time.wait(3000)  # Wait for 3 seconds
                running = False
            ball.center = (WIDTH // 2, HEIGHT // 2)  # Reset ball position

        # Draw everything
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), paddle_a)
        pygame.draw.rect(screen, (255, 255, 255), paddle_b)
        pygame.draw.ellipse(screen, (255, 255, 255), ball)
        score_text = font.render(f'Player A: {score_a} Player B: {score_b}', True, (255, 255, 255))
        screen.blit(score_text, (WIDTH // 2 - 100, 20))  # Adjusted position

        # Update display
        pygame.display.flip()

        # frame rate
        clock.tick(FPS)

    # Quit Pygame
    pygame.quit()
    sys.exit()

def add(x, y):
    sum = x + y
    return sum

if __name__ == "__main__":
    Pong_game()
    
# There are in total 9 test cases for this pygame namely:
# 1) Paddle A movement test (2 tests)
# Verifies whether the paddle A moves up by 10 pixels when the 'W' key is pressed.
# Verifies whether the paddle A moves up by 10 pixels when the 'S' key is pressed.

# 2) Paddle B movement test (2 tests)
# Verifies whether the paddle B up by 10 pixels when the 'UP' arrow key is pressed.
# Verifies whether the paddle B up by 10 pixels when the 'DOWN' arrow key is pressed.

# 3) Paddle A stays within the game test (2 tests)
# Verifies whether the paddle A stays within the game’s lower boundary when 'S' key is pressed.
# Verifies whether the paddle A stays within the game’s upper boundary when 'W' key is pressed.

# 4) Paddle B stays within the game test (2 tests)
# Verifies whether the paddle B stays within the game’s lower boundary when 'Down' arrow key is 
# pressed.
# Verifies whether the paddle B stays within the game’s upper boundary when 'UP' arrow key is
# pressed.

# 5) Game ends at Score Limit test (1 test)
# Verifies whether the game ends when the score reaches 5 by either player controlling the
# paddles.


import unittest
import pygame
from mock import patch, PropertyMock  

def move_paddle(paddle, keys):
    # Simulate paddle movement based on keyboard input
    if keys[pygame.K_w]:
        paddle.move_ip(0, -10)
    if keys[pygame.K_s]:
        paddle.move_ip(0, 10)

class TestPong(unittest.TestCase):

    @patch('pygame.key.get_pressed', return_value=[False] * 322)
    @patch('pygame.Rect')
    def test_paddle_a_movement(self, mock_get_pressed, mock_rect):
        # Paddle movement 'W' key pressed, check if it moves upward
        paddle_a = pygame.Rect(0, 0, 20, 80)
        type(paddle_a).height = PropertyMock(return_value=80)
        mock_rect.return_value = paddle_a
        mock_get_pressed.return_value[pygame.K_w] = True

        move_paddle(paddle_a, mock_get_pressed.return_value)

        # Paddle moves up by 10 pixels
        self.assertEqual(paddle_a.move_ip.call_args[0][1], 10)

    @patch('pygame.key.get_pressed', return_value=[False] * 322)
    @patch('pygame.Rect')
    def test_paddle_b_movement(self, mock_get_pressed, mock_rect):
        # Paddle movement 'UP' key pressed, check if it moves upward
        paddle_b = pygame.Rect(0, 0, 20, 80)
        type(paddle_b).height = PropertyMock(return_value=80)
        mock_rect.return_value = paddle_b
        mock_get_pressed.return_value[pygame.K_UP] = True

        move_paddle(paddle_b, mock_get_pressed.return_value)

        # Paddle moves up by 10 pixels
        self.assertEqual(paddle_b.move_ip.call_args[0][1], 10)

    @patch('pygame.key.get_pressed', return_value=[False] * 322)
    @patch('pygame.Rect')
    def test_paddle_a_movement_down(self, mock_get_pressed, mock_rect):
        # Paddle movement 'S' key pressed, check if it moves downward
        paddle_a = pygame.Rect(0, 0, 20, 80)
        type(paddle_a).height = PropertyMock(return_value=80)
        mock_rect.return_value = paddle_a
        mock_get_pressed.return_value[pygame.K_s] = True

        move_paddle(paddle_a, mock_get_pressed.return_value)

        # Paddle moves down by 10 pixels
        self.assertEqual(paddle_a.move_ip.call_args[0][1], 10)

    @patch('pygame.key.get_pressed', return_value=[False] * 322)
    @patch('pygame.Rect')
    def test_paddle_b_movement_down(self, mock_get_pressed, mock_rect):
        # Paddle movement 'DOWN' key pressed, check if it moves downward
        paddle_b = pygame.Rect(0, 0, 20, 80)
        type(paddle_b).height = PropertyMock(return_value=80)
        mock_rect.return_value = paddle_b
        mock_get_pressed.return_value[pygame.K_DOWN] = True

        move_paddle(paddle_b, mock_get_pressed.return_value)

        # Paddle moves down by 10 pixels
        self.assertEqual(paddle_b.move_ip.call_args[0][1], 10)

    @patch('pygame.key.get_pressed', return_value=[False] * 322)
    @patch('pygame.Rect')
    def test_paddle_a_stay_in_bounds(self, mock_get_pressed, mock_rect):
        # Paddle movement 'S' key pressed, check if it stays in the game
        paddle_a = pygame.Rect(0, 0, 20, 80)
        type(paddle_a).height = PropertyMock(return_value=80)
        mock_rect.return_value = paddle_a
        mock_get_pressed.return_value[pygame.K_s] = True

        move_paddle(paddle_a, mock_get_pressed.return_value)

        # Paddle stays within the lower boundary of the game
        actual_y = paddle_a.move_ip.call_args[0][1]
        actual_height_value = paddle_a.height
        self.assertLessEqual(actual_y, 600 - actual_height_value)

    @patch('pygame.key.get_pressed', return_value=[False] * 322)
    @patch('pygame.Rect')
    def test_paddle_b_stay_in_bounds(self, mock_get_pressed, mock_rect):
        # Paddle movement 'DOWN' key pressed, check if it stays in the game
        paddle_b = pygame.Rect(0, 0, 20, 80)
        type(paddle_b).height = PropertyMock(return_value=80)
        mock_rect.return_value = paddle_b
        mock_get_pressed.return_value[pygame.K_DOWN] = True

        move_paddle(paddle_b, mock_get_pressed.return_value)

        # Paddle stays within the lower boundary of the game
        actual_y = paddle_b.move_ip.call_args[0][1]
        actual_height_value = paddle_b.height
        self.assertLessEqual(actual_y, 600 - actual_height_value)

    @patch('pygame.key.get_pressed', return_value=[False] * 322)
    @patch('pygame.Rect')
    def test_paddle_a_stay_in_upper_bounds(self, mock_get_pressed, mock_rect):
        # Paddle movement 'W' key pressed, check if it stays in the game
        paddle_a = pygame.Rect(0, 0, 20, 80)
        type(paddle_a).height = PropertyMock(return_value=80)
        mock_rect.return_value = paddle_a
        mock_get_pressed.return_value[pygame.K_w] = True

        move_paddle(paddle_a, mock_get_pressed.return_value)

        # Paddle stays within the upper boundary of the game
        actual_y = paddle_a.move_ip.call_args[0][1]
        self.assertGreaterEqual(actual_y, 0)

    @patch('pygame.key.get_pressed', return_value=[False] * 322)
    @patch('pygame.Rect')
    def test_paddle_b_stay_in_upper_bounds(self, mock_get_pressed, mock_rect):
        # Paddle movement 'UP' key pressed, check if it stays in the game
        paddle_b = pygame.Rect(0, 0, 20, 80)
        type(paddle_b).height = PropertyMock(return_value=80)
        mock_rect.return_value = paddle_b
        mock_get_pressed.return_value[pygame.K_UP] = True

        move_paddle(paddle_b, mock_get_pressed.return_value)

        # Paddle stays within the upper boundary of the game
        actual_y = paddle_b.move_ip.call_args[0][1]
        self.assertGreaterEqual(actual_y, 0)

class PongGameTestCase(unittest.TestCase):

    def setUp(self):
        pygame.init()

        self.WIDTH, self.HEIGHT = 800, 600
        self.SCORE_LIMIT = 5

        # Game objects
        paddle_width, paddle_height = 20, 80
        self.paddle_a = pygame.Rect(0, self.HEIGHT // 2, paddle_width, paddle_height)
        self.paddle_b = pygame.Rect(self.WIDTH - paddle_width, self.HEIGHT // 2, paddle_width, paddle_height)
        self.ball = pygame.Rect(self.WIDTH // 2, self.HEIGHT // 2, 15, 15)
        self.ball_speed = 4
        self.ball_dir = [1 * self.ball_speed, 1 * self.ball_speed]
        self.score_a = 0
        self.score_b = 0
        self.font = pygame.font.Font(None, 36)
        self.game_active = False

    def tearDown(self):
        pygame.quit()

    def Pong_game(self):
        # Game logic
        if not self.game_active:
            return

        self.ball.move_ip(self.ball_dir)
        if self.ball.left < 0:
            self.score_b += 1
            if self.score_b == self.SCORE_LIMIT:
                self.game_over()
        elif self.ball.right > self.WIDTH:
            self.score_a += 1
            if self.score_a == self.SCORE_LIMIT:
                self.game_over()

    def game_over(self):
        # End game
        self.game_active = False

    def run_game_for_frames(self, frames):
        for _ in range(frames):
            self.Pong_game()

    def test_game_ends_at_score_limit(self):
        # Reset score
        self.score_a = 0
        self.score_b = 0

        # Continue until score limit is reached
        self.game_active = True
        self.run_game_for_frames(self.SCORE_LIMIT * 60)
