import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))

background = pygame.image.load("img/space-background.png")

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("img/ufoIcon.png")
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load("img/player.png")
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load("img/enemy.png")
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 150)
enemyX_change = 0.1
enemyY_change = 40

# Bullet
# Ready - you can't see the bullet on the screen
# Fire - The bullet is currently moving
bulletImg = pygame.image.load('img/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 1
bullet_state = "ready"


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("left arrow is pressed")
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                print("right arrow is pressed")
                playerX_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    print("space is pressed")
                    # bulletSound = mixer.Sound("laser.wav")
                    # bulletSound.play()
                    # Get the current x cordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                print("key stroke has been released")
                playerX_change = 0.0

    # checks boundaries of player
    playerX += playerX_change

    if playerX < 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # enemy movement
    enemyX += enemyX_change

    if enemyX < 0:
        enemyX_change = 0.1
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.1
        enemyY += enemyY_change

    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
