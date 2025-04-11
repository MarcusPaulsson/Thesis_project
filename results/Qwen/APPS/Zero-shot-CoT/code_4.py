def find_lucky_time(x, hh, mm):
    def is_lucky(time):
        return '7' in time

    def time_to_string(total_minutes):
        hours = total_minutes // 60
        minutes = total_minutes % 60
        return f"{hours:02}:{minutes:02}"

    wake_up_time = hh * 60 + mm
    for y in range(wake_up_time // x + 1):
        alarm_time = wake_up_time - x * y
        if alarm_time < 0:
            alarm_time += 24 * 60
        if is_lucky(time_to_string(alarm_time)):
            return y

x = int(input())
hh, mm = map(int, input().split())
print(find_lucky_time(x, hh, mm))