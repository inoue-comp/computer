import pygame
import sys
import random
import os
import time

# 初期設定
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
pygame.init()
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blackjack")

# カラー定義
GREEN = (0, 128, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# フォント設定
FONT = pygame.font.SysFont(None, 40)

# 画像読み込み
card_images = {i: pygame.image.load(f"png/{i}.png") for i in range(1, 56)}





##============================================各種関数定義
# --- 山札を生成する ---
def create_deck():
    deck = list(range(1, 52))
    random.shuffle(deck)
    return deck

# --- カードの数値（1～13）を返す ---
def card_value(card):
    value = card % 13
    if value == 0:
        value = 13
    return value

# --- スコアを計算する ---
def calc_score(cards):
    values = []
    for c in cards:
        v = card_value(c)
        if v > 10:  # J,Q,K
            v = 10
        values.append(v)

    total = sum(values)
    aces = values.count(1)
    # Aを11として使えるだけ使う（21を超えない範囲で）
    while aces > 0 and total + 10 <= 21:
        total += 10
        aces -= 1
    return total

# --- カードを1枚引く ---
def draw_card(deck, marker):
    card = deck[marker]
    return card, marker + 1

# --- 勝敗を判定する ---
def judge(player_score, dealer_score):
    if player_score > 21:
        print("あなたのバースト。あなたの負けです。")
        return 4 #
    elif dealer_score > 21:
        print("ディーラーのバースト。あなたの勝ちです。")
        return 0 #
    elif player_score > dealer_score:
        print("あなたの勝ちです。")
        return 1 #
    elif player_score < dealer_score:
        print("あなたの負けです。")
        return 3 #
    else:
        print("引き分けです。")
        return 2 # 
        
# ボタン配置
def draw_button(rect, text):
    pygame.draw.rect(SCREEN, GRAY, rect, border_radius=10)
    pygame.draw.rect(SCREEN, BLACK, rect, width=2, border_radius=10)
    text_surface = FONT.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=rect.center)
    SCREEN.blit(text_surface, text_rect) 

def set_card(pos,num,cards=None):
    ##新しく定義しました!
    ##pos==0>上側、1>下側
    ##numでx枚目。歯抜けなし。
    CARD_WIDTH, CARD_HEIGHT = 111, 161
    for i in range(num):
        x,y = 50+150*i,80+pos*200
        pygame.draw.rect(SCREEN, WHITE, pygame.Rect(x,y,CARD_WIDTH, CARD_HEIGHT), border_radius=12)
        pygame.draw.rect(SCREEN, BLACK, pygame.Rect(x,y,CARD_WIDTH, CARD_HEIGHT), 3, border_radius=12)
        if cards and i < len(cards):
            img = card_images[cards[i]]
            SCREEN.blit(img, (x, y))        
##============================================各種関数定義終了



def main():
    deck = create_deck()
    marker = 0

    # ボタン設定
    button_width, button_height = 150, 60
    hit_button_rect = pygame.Rect(WIDTH//2 - 200, HEIGHT - 120, button_width, button_height)
    stand_button_rect = pygame.Rect(WIDTH//2 + 50, HEIGHT - 120, button_width, button_height)

    # 初期配布
    dealercard = []
    playercard = []
    for _ in range(2):
        card, marker = draw_card(deck, marker)
        dealercard.append(card)
        card, marker = draw_card(deck, marker)
        playercard.append(card)
    ##初期配置
    ##=====================読み込みをリニューアルしました。 new!

    ##消しました!!
    #print(d1,d2,p1,p2)
    #d1img =  pygame.image.load(d1)
    #d2img =  pygame.image.load(d2)
    #p1img =  pygame.image.load(p1)
    #p2img =  pygame.image.load(p2)
    #bkimg =  pygame.image.load(back)
    player_score = calc_score(playercard)
    dealer_score = calc_score(dealercard)
    pWinflg = False
    dWinflg = False
    if player_score == 21:
        print("あなたのブラックジャック!")
        pWinflg = True
    elif dealer_score == 21:
        pWinflg = False
        print("ディーラーのブラックジャック!　あなたの負けです。")
        dWinflg = True
    hitmarker1 = False
    standmarker1 = False    
    clock = pygame.time.Clock()
    ##最初のループ
    running = True
    while running:
        SCREEN.fill(GREEN)
        # 台紙枠の描画
        set_card(1,2,playercard)
        set_card(0,2,dealercard)
        ##消しました!!
        #SCREEN.blit(d1img,dcard_rect1)
        #SCREEN.blit(d2img,dcard_rect2)
        #SCREEN.blit(p1img,pcard_rect1)
        #SCREEN.blit(p2img,pcard_rect2)         
        # ボタン描画
        draw_button(hit_button_rect, "HIT")
        draw_button(stand_button_rect, "STAND")



        # イベント処理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if hit_button_rect.collidepoint(event.pos):
                    hitmarker1 = True
                    print("HIT pressed")                    
                    card, marker = draw_card(deck, marker)
                    playercard.append(card)
                    ##消しました!!
                    #pygame.draw.rect(SCREEN, WHITE, pcard_rect3, border_radius=12)
                    #pygame.draw.rect(SCREEN, BLACK, pcard_rect3, 3, border_radius=12)                    
                    #p3 =  'png\\'+str(playercard[2])+'.png'
                    #p3img =  pygame.image.load(p3)
                    #SCREEN.blit(p3img,pcard_rect3)
                    ##======================改修しました。
                    set_card(1,3,playercard)
                    ##======================
                    pygame.display.flip()
                    running = False
                    player_score = calc_score(playercard)
                    if player_score > 21:
                        print("あなたのバースト。あなたの負けです。")                    
                    break
                elif stand_button_rect.collidepoint(event.pos):
                    print("STAND pressed")
                    standmarker1 = True                    
                    running = False
                    break
        pygame.display.flip()
        clock.tick(60)
    pygame.time.delay(3000)
    dcnt = 0
    while dealer_score < 17:
        card, marker = draw_card(deck, marker)
        dealercard.append(card)
        dealer_score = calc_score(dealercard)
        dcnt +=1
    if dealer_score > 21:
       print("ディーラーのバースト。あなたの勝ちです。")
       pWinflg = True
    if judge(player_score,dealer_score) <2:
        print("You Win")
    if hitmarker1 == True:
       set_card(1,3,playercard)
    else:
        set_card(1,2,playercard)
    set_card(0,2+dcnt,dealercard)
    pygame.display.flip()
    clock.tick(60)

if __name__ == "__main__":
    main()