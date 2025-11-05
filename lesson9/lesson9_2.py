import pygame
import sys
import random
import os
import time
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
pygame.init()

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
# 初期設定
pygame.init()
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blackjack")
deck = create_deck()
marker = 0

# カラー定義
GREEN = (0, 128, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# フォント設定
FONT = pygame.font.SysFont(None, 40)

# 台紙のサイズと位置
CARD_WIDTH, CARD_HEIGHT = 111, 161
dcard_rect1 = pygame.Rect(50,80,CARD_WIDTH,CARD_HEIGHT)
dcard_rect2 = pygame.Rect(200,80,CARD_WIDTH,CARD_HEIGHT)
dcard_rect3 = pygame.Rect(350,80,CARD_WIDTH,CARD_HEIGHT)
pcard_rect1 = pygame.Rect(50,280,CARD_WIDTH,CARD_HEIGHT)
pcard_rect2 = pygame.Rect(200,280,CARD_WIDTH,CARD_HEIGHT)
pcard_rect3 = pygame.Rect(350,280,CARD_WIDTH,CARD_HEIGHT)

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
d1 = 'png\\'+str(dealercard[0])+'.png'
d2 = 'png\\'+str(dealercard[1])+'.png'
p1 = 'png\\'+str(playercard[0])+'.png'
p2 =  'png\\'+str(playercard[1])+'.png'
back =  'png\\'+'55.png'

print(d1,d2,p1,p2)
d1img =  pygame.image.load(d1)
d2img =  pygame.image.load(d2)
p1img =  pygame.image.load(p1)
p2img =  pygame.image.load(p2)
bkimg =  pygame.image.load(back)
player_score = calc_score(playercard)
dealer_score = calc_score(dealercard)
pWinflg = False
dWinflg = False

def main():
    global marker
    global pWinflg
    global dWinflg
    global dealer_score
    global player_score
    hitmarker1 = False
    standmarker1 = False    
    clock = pygame.time.Clock()
    ##最初のループ
    running = True
    while running:
        SCREEN.fill(GREEN)
        # 台紙枠の描画
        # ボタンのように後で関数化する
        pygame.draw.rect(SCREEN, WHITE, pcard_rect1, border_radius=12)
        pygame.draw.rect(SCREEN, BLACK, pcard_rect1, 3, border_radius=12)
        pygame.draw.rect(SCREEN, WHITE, pcard_rect2, border_radius=12)
        pygame.draw.rect(SCREEN, BLACK, pcard_rect2, 3, border_radius=12)
        pygame.draw.rect(SCREEN, WHITE, dcard_rect1, border_radius=12)
        pygame.draw.rect(SCREEN, BLACK, dcard_rect1, 3, border_radius=12)
        pygame.draw.rect(SCREEN, WHITE, dcard_rect2, border_radius=12)
        pygame.draw.rect(SCREEN, BLACK, dcard_rect2, 3, border_radius=12)
        SCREEN.blit(d1img,dcard_rect1)
        SCREEN.blit(d2img,dcard_rect2)
        SCREEN.blit(p1img,pcard_rect1)
        SCREEN.blit(p2img,pcard_rect2)         

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
                    print("Hit pressed")                    
                elif stand_button_rect.collidepoint(event.pos):
                    standmarker1 = True                    
                    print("STAND pressed")
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()