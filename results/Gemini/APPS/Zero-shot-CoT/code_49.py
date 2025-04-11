k = int(input())

length = 1
count = 9

while k > length * count:
  k -= length * count
  length += 1
  count *= 10

number = 10**(length - 1) + (k - 1) // length
index = (k - 1) % length

print(str(number)[index])