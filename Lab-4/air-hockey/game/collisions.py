"""Robust circle-circle collision response for puck and paddle."""
import math

def handle_paddle_collision(puck, paddle):
    dx = puck.x - paddle.x
    dy = puck.y - paddle.y
    min_distance = puck.radius + paddle.radius
    distance_sq = dx * dx + dy * dy
    if distance_sq >= min_distance * min_distance:
        return False

    distance = math.sqrt(distance_sq)
    if distance < 1e-9:
        # Deterministic fallback normal if the circles are exactly concentric.
        nx, ny = (1.0, 0.0) if puck.vx <= 0 else (-1.0, 0.0)
        distance = 0.0
    else:
        nx, ny = dx / distance, dy / distance

    # Separate the overlapping circles so they cannot repeatedly collide in place.
    overlap = min_distance - distance
    puck.x += nx * (overlap + 0.5)
    puck.y += ny * (overlap + 0.5)

    # Reflect only when the puck is moving into the paddle along the collision normal.
    normal_speed = puck.vx * nx + puck.vy * ny
    if normal_speed < 0:
        puck.vx -= 2 * normal_speed * nx
        puck.vy -= 2 * normal_speed * ny
    else:
        # If already separating, don't reverse it again.
        return True

    # A small, bounded speed increase makes rallies lively without unbounded acceleration.
    speed = math.hypot(puck.vx, puck.vy)
    if speed > 0:
        target_speed = min(speed * 1.025, 10.0)
        puck.vx = puck.vx / speed * target_speed
        puck.vy = puck.vy / speed * target_speed
    return True
