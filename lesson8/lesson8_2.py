import random

# --- 山札を生成する ---
def create_deck():
    deck = list(range(1, 53))
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
        return "あなたのバースト。あなたの負けです。"
    elif dealer_score > 21:
        return "ディーラーのバースト。あなたの勝ちです。"
    elif player_score > dealer_score:
        return "あなたの勝ちです。"
    elif player_score < dealer_score:
        return "あなたの負けです。"
    else:
        return "引き分けです。"

# --- メインゲーム ---
def play_blackjack():
    deck = create_deck()
    marker = 0

    # 初期配布
    dealercard = []
    playercard = []
    for _ in range(2):
        card, marker = draw_card(deck, marker)
        dealercard.append(card)
        card, marker = draw_card(deck, marker)
        playercard.append(card)

    # スコア計算
    pscore = calc_score(playercard)
    dscore = calc_score([dealercard[0]])  # 1枚だけ見せる

    print("ディーラーのカードの1枚目は", card_value(dealercard[0]))
    print("あなたのカード合計は", pscore)

    # --- プレイヤーターン ---
    while True:
        if pscore == 21:
            print("あなたのブラックジャック！")
            break
        print("スタンドなら1、ヒットなら2を入力してください。")
        try:
            select = int(input("> "))
        except ValueError:
            print("1 または 2 を入力してください。")
            continue
        if select not in (1, 2):
            print("1 または 2 を入力してください。")
            continue

        if select == 1:
            break
        elif select == 2:
            card, marker = draw_card(deck, marker)
            playercard.append(card)
            pscore = calc_score(playercard)
            print("あなたの引いたカードは", card_value(card))
            print("あなたのカード合計は", pscore)
            if pscore >= 21:
                break

    # --- ディーラーターン ---
    print("\nディーラーの2枚目は", card_value(dealercard[1]))
    dscore = calc_score(dealercard)
    print("ディーラーのカード合計は", dscore)

    while dscore < 17:
        card, marker = draw_card(deck, marker)
        dealercard.append(card)
        dscore = calc_score(dealercard)
        print("ディーラーがカードを引きました。現在の合計は", dscore)

    # --- 勝敗判定 ---
    print("\nあなたの最終スコア:", pscore)
    print("ディーラーの最終スコア:", dscore)
    print(judge(pscore, dscore))

# 実行
if __name__ == "__main__":
    play_blackjack()