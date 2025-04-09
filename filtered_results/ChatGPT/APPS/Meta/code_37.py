a, b, c = map(int, input().split())

# Check all possible combinations of shots from Ebony and Ivory
for x in range(c // a + 1):
    if (c - x * a) % b == 0:
        print("Yes")
        break
else:
    print("No")