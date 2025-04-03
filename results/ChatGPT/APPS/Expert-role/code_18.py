from collections import deque

s = input().strip()
t = deque()
u = []

for char in s:
    t.append(char)

while t:
    # Find the smallest character in the remaining part of t
    min_char = min(t)
    # Find the index of the first occurrence of this character
    min_index = t.index(min_char)
    
    # Move characters from t to u until we reach the min_char
    for _ in range(min_index + 1):
        u.append(t.popleft())
    
    # Move the min_char to u
    u.append(t.popleft())

# Join the list to form the final string u
print(''.join(u))