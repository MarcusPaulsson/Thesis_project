def calculate_midpoint(start_time, end_time):
    # Convert start and end times to total minutes
    start_minutes = start_time[0] * 60 + start_time[1]
    end_minutes = end_time[0] * 60 + end_time[1]
    
    # Calculate midpoint in total minutes
    midpoint_minutes = (start_minutes + end_minutes) // 2
    
    # Convert back to hours and minutes
    h3 = midpoint_minutes // 60
    m3 = midpoint_minutes % 60
    
    return h3, m3

def parse_time(time_str):
    return tuple(map(int, time_str.split(':')))

def format_time(h, m):
    return f"{h:02}:{m:02}"

# Read input
start_time = parse_time(input().strip())
end_time = parse_time(input().strip())

# Calculate midpoint
midpoint = calculate_midpoint(start_time, end_time)

# Print result in the required format
print(format_time(*midpoint))