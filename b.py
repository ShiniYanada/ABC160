x = int(input())
sum = 0
sum += (x // 500) * 1000
x = x - (x // 500) * 500
sum += (x // 5) * 5
print(sum)
