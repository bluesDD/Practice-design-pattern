# 数値にして、順番逆にして、3番目を出力する

target = [4, 18, 25, 20, "9", "40"]
target = list(map(int, target))
print(sorted(target, reverse=True)[3])

sub = [6,1,5,6,3,2,6]
a = [print(1) for _ in range(len(sub))]
print(a)
flag = False
candidate = []
