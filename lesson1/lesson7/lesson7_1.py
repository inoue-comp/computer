##pygameのインポートはpygame系全ての基本
import pygame

##pygame初期処理(おまじない)
pygame.init()

##スクリーンの作成
screen = pygame.display.set_mode((640, 480))

##スクリーンのキャプション設定
pygame.display.set_caption("はじめてのPygame")

##runningは特に意味のないboolean型として設定
##running=Trueの時のみゲーム運用中
running = True
while running:
    ##何かイベントを取得すればそのたびに
    for event in pygame.event.get():
        ##それがゲーム終了であれば、ループをやめる
        if event.type == pygame.QUIT:
            running = False
    ##画面を黒で塗りつぶす    
    screen.fill((0, 0, 0))  # 黒で塗りつぶし
    ##表示を更新する
    pygame.display.update()

pygame.quit()
