def calculate_midpoint_time(start_time: str, end_time: str) -> str:
    h1, m1 = map(int, start_time.split(':'))
    h2, m2 = map(int, end_time.split(':'))

    # Convert start and end time to total minutes
    start_minutes = h1 * 60 + m1
    end_minutes = h2 * 60 + m2

    # Calculate the midpoint in total minutes
    midpoint_minutes = (start_minutes + end_minutes) // 2

    # Convert back to hours and minutes, ensuring to handle overflow properly
    h3 = (midpoint_minutes // 60) % 24  # Use % 24 to wrap around hours
    m3 = midpoint_minutes % 60

    # Return the result in the required format
    return f"{h3:02}:{m3:02}"

# Example usage
start_time = input("Enter start time (HH:MM): ")
end_time = input("Enter end time (HH:MM): ")
print(calculate_midpoint_time(start_time, end_time))