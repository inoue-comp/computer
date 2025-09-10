
#リストの扱い

fruits = ["りんご", "バナナ", "みかん"]

#末尾追加
fruits.append("なし")
print(fruits[3])  # → なし
print(len(fruits))  # → 4

#任意箇所追加
fruits.insert(0,"ぶどう")
print(fruits[0])  # → ぶどう
print(len(fruits))  # → 5

#リスト接続
fruits.extend(["かき","もも"])
print(fruits[5])  # → かき
print(len(fruits))  # → 7

#リスト反転
fruits.reverse()
print(fruits[0])  # → もも
print(len(fruits))  # → 7

#末尾放出
print(fruits.pop())  # → ぶどう
print(len(fruits))  # → 6

#要素削除
print(fruits[1])  # → かき
del fruits[1]
print(len(fruits))
print(fruits[1])  # → なし

#リストクリア
fruits.clear()
print(len(fruits))  # → 0

#2次元配列
fruits = ["りんご", "バナナ", "みかん"]
fruits2 = ["ぶどう","なし","もも"]
fruits.append(fruits2)
print(fruits[3])  # → なし
print(fruits[3][2])  # → なし
print(len(fruits))  # → 4
