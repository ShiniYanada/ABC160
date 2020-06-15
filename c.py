k, n = list(map(int, input().split()))
houses = list(map(int, input().split()))
distance = 0
for i in range(n):
  if i == n-1:
    tmp = abs(houses[0] - houses[i])
  else:
    tmp = abs(houses[i] - houses[i+1])
  tmp = min(tmp, k - tmp)
  if tmp > distance:
    distance = tmp
print(k - distance)
