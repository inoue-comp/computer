##pygameのインポートはpygame系全ての基本
import pygame
import os
import sys
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("はじめてのPygame")
running = True
bg = pygame.image.load("bg.png")                ##-----------add
player_img = pygame.image.load("player.png")
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))                     ##-----------add
    screen.blit(player_img, (100, 100))
    pygame.display.update()

pygame.quit()
