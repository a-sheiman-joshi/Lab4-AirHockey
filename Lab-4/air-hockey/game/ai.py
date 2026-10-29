"""Simple computer opponent with a little reaction delay and aiming error."""
import random
SPEED = 3.5
REACTION_DELAY_FRAMES = 6
TRACKING_ERROR = 18

class ComputerAI:
    def __init__(self, speed=SPEED):
        self.speed = speed
        self.reaction_delay = REACTION_DELAY_FRAMES
        self.tracking_error = TRACKING_ERROR
        self._delay_counter = 0
        self._target_y = None

    def update(self, paddle, puck):
        if self._target_y is None or self._delay_counter <= 0:
            self._target_y = puck.y + random.uniform(-self.tracking_error, self.tracking_error)
            self._delay_counter = self.reaction_delay
        else:
            self._delay_counter -= 1
        if self._target_y < paddle.y - 2:
            paddle.move_by(0, -self.speed)
        elif self._target_y > paddle.y + 2:
            paddle.move_by(0, self.speed)
