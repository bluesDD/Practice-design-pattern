# 数値にして、順番逆にして、3番目を出力する

target = [4, 18, 25, 20, "9", "40"]
target = list(map(int, target))
print(sorted(target, reverse=True)[3])
