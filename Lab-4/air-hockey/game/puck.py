"""Puck: the disc players hit into the opponent's goal."""
class Puck:
    def __init__(self, x, y, radius=12):
        self.x, self.y, self.radius = float(x), float(y), radius
        self.vx = 0.0
        self.vy = 0.0

    def move(self):
        self.x += self.vx
        self.y += self.vy

    def bounce_off_walls(self, height, margin):
        if self.y - self.radius < margin:
            self.y = margin + self.radius
            self.vy = abs(self.vy)
        elif self.y + self.radius > height - margin:
            self.y = height - margin - self.radius
            self.vy = -abs(self.vy)
