def minimum_time(n, tasks):
    # Sort both the tasks and students' laziness levels
    tasks.sort()
    tasks.reverse()  # To minimize the time, we pair the largest with the largest
    students = tasks.copy()
    students.sort()
    
    total_time = 0
    for i in range(n):
        total_time += students[i] * tasks[i]
        total_time %= 10007  # Take modulo at each step to avoid overflow

    return total_time

# Input reading
n = int(input())
tasks = [int(input()) for _ in range(n)]

# Calculate and print the result
result = minimum_time(n, tasks)
print(result)