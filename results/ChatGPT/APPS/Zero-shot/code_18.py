from collections import deque

s = input().strip()
t = deque()
u = []

for char in s:
    t.append(char)

while t:
    # Check the smallest character in t and the remaining characters in s
    min_char = min(t)
    # If the front character in s is smaller or equal to min_char, we can add it to t
    while s and (not t or s[0] <= min_char):
        t.appendleft(s[0])
        s = s[1:]
        min_char = min(t)  # Update min_char after adding to t
        
    # Extract the last character from t to append to u
    u.append(t.pop())

# Join the list into a string and print the result
print(''.join(u[::-1]))  # Reverse u to get the correct order