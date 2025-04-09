h1, m1 = map(int, input().replace(':', ' ').split())
h2, m2 = map(int, input().replace(':', ' ').split())

start_minutes = h1 * 60 + m1
end_minutes = h2 * 60 + m2

mid_minutes = (start_minutes + end_minutes) // 2

h3 = mid_minutes // 60
m3 = mid_minutes % 60

print(f"{h3:02d}:{m3:02d}")