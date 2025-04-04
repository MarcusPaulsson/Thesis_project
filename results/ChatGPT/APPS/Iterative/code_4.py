def is_lucky(h, m):
    return '7' in f"{h:02d}{m:02d}"

def time_before(hh, mm, x):
    mm -= x
    if mm < 0:
        mm += 60
        hh -= 1
    if hh < 0:
        hh += 24
    return hh, mm

def main():
    x = int(input("Enter the number of minutes to go back: "))
    hh, mm = map(int, input("Enter the current time (hh mm): ").split())

    if not (0 <= hh < 24 and 0 <= mm < 60):
        print("Invalid time format. Please enter hours (0-23) and minutes (0-59).")
        return

    y = 0
    while not is_lucky(hh, mm):
        hh, mm = time_before(hh, mm, x)
        y += 1

    print(y)

if __name__ == "__main__":
    main()