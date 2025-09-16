import random

#関数の複層利用

#Wizardry(最古のRPGの一つ)を参考にダメージ計算プログラムを書いてみる。

#1からnまでの数をランダムに得る。さいころを投げているような図式
def roll(n):
    return random.randint(1,n)

#八面体サイコロ+4点ダメージ。
def damage():
    return roll(8)+4

#20面体サイコロを振った目がキャラクタごとの命中基準値-相手のAC以上なら命中。
#ここでは何回命中したかを返している。
#Thac0(ﾀｺ)はACが0の時に命中させるために必要なキャラクタごとの命中基準値
#ACは防御力。低いほど防御性能が良い。20が最低値。
def HitCheck(Thac0,AtkN,AC):
    i = 0
    for j in range(AtkN):
        if roll(20) >=Thac0 - AC:
            i = i+1
    return i

#攻撃判定処理をここでまとめて行っている。    
def Hit():   
    x = HitCheck(15,3,5)
    n = 0
    if x > 0:
        for i in range(x):
            n = n + damage()
    return n

print("戦士は剣で" + str(3) + "回突いて、"+ str(Hit()) +"ダメージ。")