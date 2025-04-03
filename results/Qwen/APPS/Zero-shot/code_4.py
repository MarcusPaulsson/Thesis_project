def find_lucky_time(x, hh, mm):
    y = 0
    while True:
        current_time = hh * 60 + mm - x * y
        if current_time < 0:
            current_time += 24 * 60
        if '7' in str(current_time // 60).zfill(2) + str(current_time % 60).zfill(2):
            return y
        y += 1

x = int(input())
hh, mm = map(int, input().split())
print(find_lucky_time(x, hh, mm))