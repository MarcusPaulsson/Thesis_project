def max_score_in_contest(tc, test_cases):
    results = []
    
    for _ in range(tc):
        n = test_cases[_][0]
        C, T = test_cases[_][1]
        problems = test_cases[_][2]

        # Prepare a list of (difficulty, score) pairs
        problems = [(a_i, p_i) for (a_i, p_i) in problems]

        max_score = 0

        # Try all possible training times
        for train_time in range(int(T) + 1):
            s = 1.0 + C * train_time
            remaining_time = T - train_time

            score = 0
            skill = s

            # Try to solve problems in different orders
            for a_i, p_i in sorted(problems, key=lambda x: (x[0] / skill, -x[1])):
                if remaining_time <= 0:
                    break

                # Time to watch the episode
                if remaining_time < 10:
                    continue
                remaining_time -= 10
                skill *= 0.9  # Skill decreases after watching

                # Time to solve the problem
                time_to_solve = a_i / skill

                if remaining_time >= time_to_solve:
                    remaining_time -= time_to_solve
                    score += p_i
                else:
                    break

            max_score = max(max_score, score)

        results.append(max_score)

    return results


# Read input
import sys
input = sys.stdin.read
data = input().strip().split('\n')

tc = int(data[0])
test_cases = []
index = 1

for _ in range(tc):
    n = int(data[index])
    C, T = map(float, data[index + 1].split())
    problems = []

    for i in range(n):
        a_i, p_i = map(int, data[index + 2 + i].split())
        problems.append((a_i, p_i))

    test_cases.append((n, (C, T), problems))
    index += 2 + n

# Get results
results = max_score_in_contest(tc, test_cases)

# Print results
for result in results:
    print(result)