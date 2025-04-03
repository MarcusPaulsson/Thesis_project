def is_possible_visible_pips(x):
    if x < 14:
        return False
    # The minimum pips visible with at least one die is 14 (1 top + 6 sides = 5+5+4+4)
    # The rest can be multiples of 7 (which is the total change in pips from stacking)
    return (x - 14) % 7 == 0

t = int(input())
x_values = map(int, input().split())

results = []
for x in x_values:
    if is_possible_visible_pips(x):
        results.append("YES")
    else:
        results.append("NO")

print("\n".join(results))