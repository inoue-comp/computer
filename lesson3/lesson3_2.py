answer = input("1～10の数字を入れてください:")
answer = int(answer)
if answer == 5:
    print("ちょうど真ん中の値ですね")
elif answer < 5 and answer>=0:
    print("真ん中よりも小さい値ですね")
elif answer > 5 and answer<=10:
    print("真ん中よりも大きい値ですね")    
else:
    print("範囲外の値ですね")
    