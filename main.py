import pygame
import sys

# ÐÐ½ÑÑÑÐ°Ð»ÑÐ·Ð°ÑÑÑ Pygame
pygame.init()

# ÐÐ¾Ð½ÑÑÐ°Ð½ÑÐ¸ Ð´Ð»Ñ ÐµÐºÑÐ°Ð½Ñ
WIDTH, HEIGHT = 800, 600
FPS = 60

# ÐÐ¾Ð»ÑÐ¾ÑÐ¸
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Ð¡ÑÐ²Ð¾ÑÐµÐ½Ð½Ñ ÐµÐºÑÐ°Ð½Ñ
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Shooter")

# ÐÑÐ°Ð²ÐµÑÑ
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 10
player_speed = 5

# ÐÐ¾ÑÐ¾Ð³Ð¸
enemy_size = 30
enemy_speed = 3
enemies = []

# ÐÐ¾ÑÐ°ÑÐºÐ¾Ð²Ð° ÐºÑÐ»ÑÐºÑÑÑÑ Ð²Ð¾ÑÐ¾Ð³ÑÐ²
num_enemies = 5

for _ in range(num_enemies):
    enemy = pygame.Rect(
        pygame.display.get_surface().get_width() // 2,
        pygame.display.get_surface().get_height() // 2,
        enemy_size,
        enemy_size,
    )
    enemies.append(enemy)

# Ð¨ÑÐ¸ÑÑ Ð´Ð»Ñ Ð²Ð¸Ð²ÐµÐ´ÐµÐ½Ð½Ñ ÑÐ°ÑÑÐ½ÐºÑ
font = pygame.font.Font(None, 36)

# Ð Ð°ÑÑÐ½Ð¾Ðº
score = 0

# ÐÑÐ½Ð¾Ð²Ð½Ð¸Ð¹ ÑÐ¸ÐºÐ»
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Ð ÑÑ Ð³ÑÐ°Ð²ÑÑ
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    # Ð ÑÑ Ð²Ð¾ÑÐ¾Ð³ÑÐ²
    for enemy in enemies:
        enemy.y += enemy_speed
        if enemy.y > HEIGHT:
            enemy.y = 0
            enemy.x = pygame.display.get_surface().get_width() // 2

    # ÐÑÑÐºÐ½ÐµÐ½Ð½Ñ Ð²Ð¾ÑÐ¾Ð³ÑÐ² Ñ Ð³ÑÐ°Ð²ÑÑ
    for enemy in enemies:
        if pygame.Rect(player_x, player_y, player_size, player_size).colliderect(enemy):
            pygame.quit()
            sys.exit()

    # ÐÑÑÐºÐ½ÐµÐ½Ð½Ñ ÐºÑÐ»Ñ Ð³ÑÐ°Ð²ÑÑ Ñ Ð²Ð¾ÑÐ¾Ð³ÑÐ²
    for bullet in bullets:
        for enemy in enemies:
            if enemy.colliderect(bullet):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1

    # Ð
Ð°Ð»ÑÐ²Ð°Ð½Ð½Ñ
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (player_x, player_y, player_size, player_size))

    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    # ÐÐ½Ð¾Ð²Ð»ÐµÐ½Ð½Ñ ÐµÐºÑÐ°Ð½Ñ
    pygame.display.flip()

    # ÐÑÑÐ°Ð½Ð¾Ð²Ð»ÐµÐ½Ð½Ñ FPS
    clock.tick(FPS)

