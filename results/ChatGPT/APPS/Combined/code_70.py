def calculate_midpoint(start_time: str, end_time: str) -> str:
    # Parse the start and end times
    h1, m1 = map(int, start_time.split(':'))
    h2, m2 = map(int, end_time.split(':'))

    # Convert times to total minutes
    start_minutes = h1 * 60 + m1
    end_minutes = h2 * 60 + m2

    # Calculate midpoint in total minutes
    midpoint_minutes = (start_minutes + end_minutes) // 2

    # Convert midpoint back to hours and minutes
    h3 = midpoint_minutes // 60
    m3 = midpoint_minutes % 60

    # Format the result as hh:mm
    return f"{h3:02}:{m3:02}"

# Read input
start_time = input().strip()
end_time = input().strip()

# Calculate and print the midpoint
print(calculate_midpoint(start_time, end_time))