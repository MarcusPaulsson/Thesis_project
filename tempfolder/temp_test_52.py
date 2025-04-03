def min_total_time(n, tasks):
    tasks.sort()
    total_time = 0
    for i in range(n):
        total_time += tasks[i] * tasks[i]
        total_time %= 10007
    return total_time

if __name__ == "__main__":
    n = int(input())
    tasks = [int(input()) for _ in range(n)]
    result = min_total_time(n, tasks)
    print(result)