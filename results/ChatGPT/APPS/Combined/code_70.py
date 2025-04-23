def midpoint_of_contest(start_time, end_time):
    # Convert start and end times to total minutes
    start_hours, start_minutes = map(int, start_time.split(':'))
    end_hours, end_minutes = map(int, end_time.split(':'))
    
    start_total_minutes = start_hours * 60 + start_minutes
    end_total_minutes = end_hours * 60 + end_minutes
    
    # Calculate the midpoint in total minutes
    midpoint_total_minutes = (start_total_minutes + end_total_minutes) // 2
    
    # Convert back to hours and minutes
    midpoint_hours = midpoint_total_minutes // 60
    midpoint_minutes = midpoint_total_minutes % 60
    
    # Format and return the result
    return f"{midpoint_hours:02}:{midpoint_minutes:02}"

# Input reading
start_time = input().strip()
end_time = input().strip()

# Output the midpoint of the contest
print(midpoint_of_contest(start_time, end_time))