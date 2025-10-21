import pygame
import random
import math

# constants for the windows width and height values
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720

# the RGB values for the colors used in the game
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

# ---- TUNABLES FOR SPEED / VOLATILITY ----
BALL_MIN_SPEED = 0.45      # px per ms
BALL_MAX_SPEED = 1.20      # hard cap, px per ms
HIT_SPEED_MULT = 1.08      # every paddle hit speeds ball up by 8%, up to max
TIME_SPEED_MULT = 1.02     # every TIME_SPEED_INTERVAL seconds, multiply speed by this
TIME_SPEED_INTERVAL = 8.0  # seconds between global ramp steps
WALL_RANDOM_JITTER = 0.02  # small random y tweak on wall bounces (px/ms)
MIN_ABS_VY_RATIO = 0.30    # ensure |vy| >= this fraction of total speed on serve

PADDLE_SPEED = 0.65        # px per ms (a touch faster to keep up)

def clamp(v, lo, hi):
    return max(lo, min(hi, v))

def speed(vx, vy):
    return math.hypot(vx, vy)

def set_speed_with_angle(base_speed, angle_rad, going_right=True):
    # angle 0 = straight right; positive angles tilt down
    vx = math.cos(angle_rad) * base_speed
    vy = math.sin(angle_rad) * base_speed
    if not going_right:
        vx = -vx
    return vx, vy

def nudge_random_y(vy):
    return vy + random.uniform(-WALL_RANDOM_JITTER, WALL_RANDOM_JITTER)

def normalize_to_max(vx, vy, max_speed):
    s = speed(vx, vy)
    if s > max_speed and s > 0:
        scale = max_speed / s
        return vx * scale, vy * scale
    return vx, vy

def serve_random_velocity():
    # pick a random overall speed
    s = random.uniform(0.55, 0.75)  # faster starts than before
    # pick an initial angle by forcing vy to be a decent fraction of s
    min_vy = s * MIN_ABS_VY_RATIO
    vy = random.uniform(min_vy, s * 0.9) * (1 if random.randint(0, 1) else -1)
    vx = math.sqrt(max(s * s - vy * vy, 0.0001))
    # randomize horizontal direction
    if random.randint(0, 1) == 0:
        vx = -vx
    return vx, vy

def main():
    # GAME SETUP
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('PONG')

    paddle_1_rect = pygame.Rect(30, (SCREEN_HEIGHT - 100)//2, 7, 100)
    paddle_2_rect = pygame.Rect(SCREEN_WIDTH - 50, (SCREEN_HEIGHT - 100)//2, 7, 100)

    paddle_1_move = 0.0
    paddle_2_move = 0.0

    # ball starts centered (fixed Y bug)
    ball_rect = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 25, 25)

    # initial velocity (px/ms)
    ball_accel_x, ball_accel_y = serve_random_velocity()

    clock = pygame.time.Clock()
    started = False

    time_since_start = 0.0
    time_since_ramp = 0.0

    def apply_paddle_hit_effect(paddle_rect, hits_rightward):
        nonlocal ball_accel_x, ball_accel_y

        # Compute where it struck on the paddle: -1 (top) to +1 (bottom)
        rel = (ball_rect.centery - paddle_rect.centery) / (paddle_rect.height / 2.0)
        rel = clamp(rel, -1.0, 1.0)

        # Current speed -> bump it up
        s = speed(ball_accel_x, ball_accel_y)
        s = clamp(s * HIT_SPEED_MULT, BALL_MIN_SPEED, BALL_MAX_SPEED)

        # Map rel to angle up to ~45 degrees
        max_angle = math.radians(45)
        angle = rel * max_angle

        # Rebuild velocity using the angle, preserving direction
        ball_accel_x, ball_accel_y = set_speed_with_angle(s, angle, going_right=hits_rightward)

        # Small position nudge to prevent sticking
        if hits_rightward:
            ball_rect.left = paddle_rect.right + 1
        else:
            ball_rect.right = paddle_rect.left - 1

    # GAME LOOP
    while True:
        screen.fill(COLOR_BLACK)

        if not started:
            font = pygame.font.SysFont('Consolas', 30)
            text = font.render('Press Space To Start', True, COLOR_WHITE)
            text_rect = text.get_rect()
            text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            screen.blit(text, text_rect)
            pygame.display.flip()
            clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    started = True
                # PLAYER 1
                if event.key == pygame.K_w:
                    paddle_1_move = -PADDLE_SPEED
                if event.key == pygame.K_s:
                    paddle_1_move = PADDLE_SPEED
                # PLAYER 2
                if event.key == pygame.K_UP:
                    paddle_2_move = -PADDLE_SPEED
                if event.key == pygame.K_DOWN:
                    paddle_2_move = PADDLE_SPEED
            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_w, pygame.K_s):
                    paddle_1_move = 0.0
                if event.key in (pygame.K_UP, pygame.K_DOWN):
                    paddle_2_move = 0.0

        pygame.draw.rect(screen, COLOR_WHITE, paddle_1_rect)
        pygame.draw.rect(screen, COLOR_WHITE, paddle_2_rect)
        pygame.draw.rect(screen, COLOR_WHITE, ball_rect)

        # ms between frames
        delta_time_ms = clock.tick(60)
        dt = delta_time_ms  # shorthand

        # Move paddles (frame-rate independent)
        paddle_1_rect.top += paddle_1_move * dt
        paddle_2_rect.top += paddle_2_move * dt

        # Clamp paddles
        paddle_1_rect.top = clamp(paddle_1_rect.top, 0, SCREEN_HEIGHT - paddle_1_rect.height)
        paddle_2_rect.top = clamp(paddle_2_rect.top, 0, SCREEN_HEIGHT - paddle_2_rect.height)

        # Out of bounds (score) ends game for now
        if ball_rect.left <= 0 or ball_rect.left >= SCREEN_WIDTH:
            return

        # Top/bottom wall bounces
        if ball_rect.top <= 0:
            ball_accel_y = -ball_accel_y
            ball_rect.top = 0
            ball_accel_y = nudge_random_y(ball_accel_y)
            ball_accel_x, ball_accel_y = normalize_to_max(ball_accel_x, ball_accel_y, BALL_MAX_SPEED)

        if ball_rect.bottom >= SCREEN_HEIGHT:
            ball_accel_y = -ball_accel_y
            ball_rect.bottom = SCREEN_HEIGHT
            ball_accel_y = nudge_random_y(ball_accel_y)
            ball_accel_x, ball_accel_y = normalize_to_max(ball_accel_x, ball_accel_y, BALL_MAX_SPEED)

        # Paddle collisions (only if ball is towards that paddle)
        if paddle_1_rect.colliderect(ball_rect) and ball_accel_x < 0 and paddle_1_rect.left < ball_rect.left:
            apply_paddle_hit_effect(paddle_1_rect, hits_rightward=True)

        if paddle_2_rect.colliderect(ball_rect) and ball_accel_x > 0 and paddle_2_rect.left > ball_rect.left:
            apply_paddle_hit_effect(paddle_2_rect, hits_rightward=False)

        # Move the ball once game started
        if started:
            # global ramp
            time_since_start += dt / 1000.0
            time_since_ramp += dt / 1000.0
            if time_since_ramp >= TIME_SPEED_INTERVAL:
                s = clamp(speed(ball_accel_x, ball_accel_y) * TIME_SPEED_MULT, BALL_MIN_SPEED, BALL_MAX_SPEED)
                # keep direction, adjust magnitude
                ang = math.atan2(ball_accel_y, ball_accel_x)
                ball_accel_x = math.cos(ang) * s
                ball_accel_y = math.sin(ang) * s
                time_since_ramp = 0.0

            ball_rect.left += ball_accel_x * dt
            ball_rect.top  += ball_accel_y * dt

        pygame.display.update()


if __name__ == '__main__':
    main()