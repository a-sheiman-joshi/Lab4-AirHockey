"""Paddle: a player's or computer's mallet, confined to its half."""
class Paddle:
    def __init__(self, x, y, radius, min_x, max_x, min_y, max_y):
        self.x, self.y, self.radius = float(x), float(y), radius
        self.min_x, self.max_x = min_x, max_x
        self.min_y, self.max_y = min_y, max_y

    def clamp(self):
        self.x = max(self.min_x, min(self.max_x, self.x))
        self.y = max(self.min_y, min(self.max_y, self.y))

    def move_by(self, dx, dy):
        self.x += dx
        self.y += dy
        self.clamp()

    def move_to(self, x, y):
        self.x, self.y = x, y
        self.clamp()
