def is_lucky_time(hh, mm):
    return '7' in f"{hh:02d}{mm:02d}"

def find_lucky_time(x, hh, mm):
    minutes_passed = 0
    
    while True:
        if is_lucky_time(hh, mm):
            return minutes_passed // x
        
        minutes_passed += x
        mm -= x
        
        if mm < 0:
            mm += 60
            hh -= 1
            
            if hh < 0:
                hh += 24

def main():
    x = int(input())
    hh, mm = map(int, input().split())
    print(find_lucky_time(x, hh, mm))

if __name__ == "__main__":
    main()