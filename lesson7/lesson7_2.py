##pygameのインポートはpygame系全ての基本
import pygame
##-----------add start
##ファイル参照のため、作業ディレクトリをOSの基本機能を使って強制移動。
import os
import sys
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
##-----------add end

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("はじめてのPygame")
running = True
player_img = pygame.image.load("player.png")    ##-----------add
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    screen.blit(player_img, (100, 100))        ##-----------add
    pygame.display.update()

pygame.quit()
