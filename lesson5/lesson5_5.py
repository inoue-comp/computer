
list1 = ["ポーション","たいまつ","腕時計"]


while len(list1)>0:
    cnt = 0
    for i in list1:
        print(str(cnt) + ":" + i)
        cnt = cnt + 1
    item = input("どのアイテムを使う？（番号で選択）: ")
    if item.isnumeric() == True:
        item = int(item)
        if item <= len(list1)-1:
            if list1[item] == "ポーション":
                print("HPが回復した！")
                del list1[item]
            elif list1[item] == "たいまつ":
                print("辺りが明るくなった！")
                del list1[item]
            elif list1[item] == "腕時計":
                print("時間が分かった!")
                del list1[item]
        else:
            print("そのアイテムは使えない")
    else:
        print("そのアイテムは使えない")
            
print("もう何も持っていない。")
