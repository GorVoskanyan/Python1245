import random
import os

import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT

pygame.init()

fps = pygame.time.Clock()

HEIGHT = 600
WIDTH = 800

FONT = pygame.font.SysFont('Verdana', 20)

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_GREEN = (0, 255, 0)

main_display = pygame.display.set_mode((WIDTH, HEIGHT))

bg = pygame.transform.scale(pygame.image.load('background.png'), (WIDTH, HEIGHT))
bg_x1 = 0
bg_x2 = bg.get_width()
bg_move = 3

IMAGE_PATH = 'Goose'
PLAYER_IMAGES = os.listdir(IMAGE_PATH)
print(PLAYER_IMAGES)


player_size = (20, 20)
player = pygame.image.load('player.png').convert_alpha() #pygame.Surface(player_size)
# player.fill(COLOR_BLACK)
player_rect = player.get_rect()
# player_speed = [1, 1]
player_move_down = [0, 4]
player_move_right = [4, 0]
player_move_left = [-4, 0]
player_move_up = [0, -4]

def creat_enemy():
    # enemy_size = (30, 30)
    enemy = pygame.image.load('enemy.png') #pygame.Surface(enemy_size)
    # enemy.fill(COLOR_BLUE)
    enemy_rect = pygame.Rect(WIDTH,
                              random.randint(enemy.get_height(), HEIGHT - enemy.get_height()), 
                              *enemy.get_size()) 
    enemy_move = [random.randint(-8, -4), 0]
    return [enemy, enemy_rect, enemy_move]

def creat_bonus():
    # bonus_size = (30, 30)
    bonus = pygame.image.load('bonus.png').convert_alpha() #pygame.Surface(bonus_size)
    # bonus.fill(COLOR_GREEN)
    bonus_width = bonus.get_width()
    bonus_rect = pygame.Rect(random.randint(bonus_width, WIDTH - bonus_width),
                              -bonus.get_height(), 
                              *bonus.get_size())
    bonus_move = [0, random.randint(4, 8)]
    return [bonus, bonus_rect, bonus_move]

CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)
CREAT_BONUS = pygame.USEREVENT + 2 == pygame.USEREVENT + 1
pygame.time.set_timer(CREAT_BONUS, 3000)
CHANGE_IMAGE = pygame.USEREVENT + 3
pygame.time.set_timer(CHANGE_IMAGE, 200)



enemies = []
bonuses =[]

score = 0

image_index = 0

playing = True

while playing:
    fps.tick(500)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
        if event.type == CREATE_ENEMY:
            enemies.append(creat_enemy())
        if event.type == CREAT_BONUS:
            bonuses.append(creat_bonus())
        if event.type == CHANGE_IMAGE:
            player = pygame.image.load(os.path.join(IMAGE_PATH, PLAYER_IMAGES [image_index]))
            image_index += 1
            if image_index >= len(PLAYER_IMAGES):
                image_index = 0
        
    # main_display.fill(COLOR_BLACK)
    bg_x1 -= bg_move
    bg_x2 -= bg_move
    
    if bg_x1 < -bg.get_width():
        bg_x1 = bg.get_width()

    if bg_x2 < -bg.get_width():
        bg_x2 =bg.get_width()

    # main_display.blit(bg, (0, 0))
    main_display.blit(bg, (bg_x1, 0))
    main_display.blit(bg, (bg_x2, 0))
    

    keys = pygame.key.get_pressed()
        
    if keys[K_DOWN] and player_rect.bottom < HEIGHT:
        player_rect = player_rect.move(player_move_down)

    if keys[K_RIGHT] and player_rect.right < WIDTH:
        player_rect = player_rect.move(player_move_right)   

    if keys[K_LEFT] and player_rect.left > 0:
        player_rect = player_rect.move(player_move_left)

    if keys[K_UP] and player_rect.top > 0:
        player_rect = player_rect.move(player_move_up)    
        #  print(player_rect)

    for enemy in enemies:
        enemy[1] = enemy[1].move(enemy[2])
        main_display.blit(enemy[0], enemy[1])

        if player_rect.colliderect(enemy[1]):
            # print('Boom')
            playing = False

    for bonus in bonuses:
        bonus[1] = bonus[1].move(bonus[2])
        main_display.blit(bonus[0], bonus[1])

        if player_rect.colliderect(bonus[1]):
            score += 1
            # print('Yep')
            bonuses.pop(bonuses.index(bonus))
    
    main_display.blit(FONT.render(str(score), True, COLOR_BLACK), (WIDTH -50, 20))
    main_display.blit(player, player_rect)
 
    # main_display.blit(enemy, enemy_rect)
    
    # print(len(enemies))

    pygame.display.flip()

    for enemy in enemies:
        if enemy[1].right < 0:
            enemies.pop(enemies.index(enemy))

    for bonus in bonuses:
        if bonus[1].top > HEIGHT:
            bonuses.pop(bonuses.index(bonus))