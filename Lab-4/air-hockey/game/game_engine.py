"""Game engine: physics, scoring, timer, goal handling and rendering."""
import random
import time
from game.puck import Puck
from game.paddle import Paddle
from game.ai import ComputerAI
from game.collisions import handle_paddle_collision
from game.renderer import WIDTH, HEIGHT, MARGIN, GOAL_TOP, GOAL_BOTTOM, draw_text, draw_banner

PLAYER_SPEED = 6
PUCK_RADIUS = 12
PADDLE_RADIUS = 28
INITIAL_PUCK_SPEED = 4.5
MATCH_DURATION = 30.0

class GameEngine:
    def __init__(self):
        self.puck = Puck(WIDTH / 2, HEIGHT / 2, PUCK_RADIUS)
        self.player = Paddle(WIDTH * .15, HEIGHT / 2, PADDLE_RADIUS,
            MARGIN + PADDLE_RADIUS, WIDTH / 2 - PADDLE_RADIUS,
            MARGIN + PADDLE_RADIUS, HEIGHT - MARGIN - PADDLE_RADIUS)
        self.computer = Paddle(WIDTH * .85, HEIGHT / 2, PADDLE_RADIUS,
            WIDTH / 2 + PADDLE_RADIUS, WIDTH - MARGIN - PADDLE_RADIUS,
            MARGIN + PADDLE_RADIUS, HEIGHT - MARGIN - PADDLE_RADIUS)
        self.ai = ComputerAI()
        self.player_score = 0
        self.computer_score = 0
        self.duration = MATCH_DURATION
        self.start_time = time.monotonic()
        self.game_over = False
        self.result = ""
        self._launch_puck()

    def _launch_puck(self):
        angle = random.choice([-.6, -.3, .3, .6])
        direction = random.choice([-1, 1])
        self.puck.vx = INITIAL_PUCK_SPEED * direction * (1 / (1 + angle*angle)**0.5)
        self.puck.vy = INITIAL_PUCK_SPEED * angle * (1 / (1 + angle*angle)**0.5)

    def _reset_puck(self):
        self.puck.x, self.puck.y = WIDTH / 2, HEIGHT / 2
        self.puck.vx = self.puck.vy = 0.0
        self._launch_puck()

    def restart(self):
        self.player_score = self.computer_score = 0
        self.start_time = time.monotonic()
        self.game_over = False
        self.result = ""
        self.player.move_to(WIDTH * .15, HEIGHT / 2)
        self.computer.move_to(WIDTH * .85, HEIGHT / 2)
        self._reset_puck()

    def handle_input(self, keys_pressed):
        import pygame
        if self.game_over:
            return
        dx = dy = 0
        if keys_pressed[pygame.K_UP]: dy -= PLAYER_SPEED
        if keys_pressed[pygame.K_DOWN]: dy += PLAYER_SPEED
        if keys_pressed[pygame.K_LEFT]: dx -= PLAYER_SPEED
        if keys_pressed[pygame.K_RIGHT]: dx += PLAYER_SPEED
        self.player.move_by(dx, dy)

    def _remaining_time(self):
        return max(0.0, self.duration - (time.monotonic() - self.start_time))

    def update(self):
        if self.game_over:
            return
        if self._remaining_time() <= 0:
            self.game_over = True
            if self.player_score > self.computer_score:
                self.result = "YOU WIN!"
            elif self.computer_score > self.player_score:
                self.result = "COMPUTER WINS!"
            else:
                self.result = "DRAW!"
            return

        self.ai.update(self.computer, self.puck)
        self.puck.move()
        self.puck.bounce_off_walls(HEIGHT, MARGIN)
        handle_paddle_collision(self.puck, self.player)
        handle_paddle_collision(self.puck, self.computer)
        self._handle_goals()

    def _handle_goals(self):
        # Score only when the puck crosses an end line inside the goal opening.
        if self.puck.x + self.puck.radius < MARGIN:
            if GOAL_TOP < self.puck.y < GOAL_BOTTOM:
                self.computer_score += 1
                self._reset_puck()
            else:
                self.puck.x = MARGIN + self.puck.radius
                self.puck.vx = abs(self.puck.vx)
        elif self.puck.x - self.puck.radius > WIDTH - MARGIN:
            if GOAL_TOP < self.puck.y < GOAL_BOTTOM:
                self.player_score += 1
                self._reset_puck()
            else:
                self.puck.x = WIDTH - MARGIN - self.puck.radius
                self.puck.vx = -abs(self.puck.vx)

    def draw(self, surface, font):
        from game import renderer
        renderer.draw_table(surface)
        renderer.draw_paddle(surface, self.player, renderer.COLOR_PLAYER)
        renderer.draw_paddle(surface, self.computer, renderer.COLOR_COMPUTER)
        renderer.draw_puck(surface, self.puck)
        remaining = int(self._remaining_time() + 0.999)
        draw_text(surface, font, f"YOU  {self.player_score}", (WIDTH//2 - 150, 28), renderer.COLOR_PLAYER)
        draw_text(surface, font, f"CPU  {self.computer_score}", (WIDTH//2 + 35, 28), renderer.COLOR_COMPUTER)
        draw_text(surface, font, f"TIME  {remaining:02d}s", (WIDTH//2 - 48, HEIGHT - 48))
        if self.game_over:
            draw_banner(surface, font, self.result + "  (Press R to restart)")
