direction = input("あなたは森の中にいます。道が右と左に別れています。行く方向は右か左かどちらですか?:")
if direction == "左":
    print("クマに出会った！ ゲームオーバー")
elif direction == "右":
    print("宝箱を見つけた！ おめでとう！")
else:
    print("道に迷ってしまった…")
    