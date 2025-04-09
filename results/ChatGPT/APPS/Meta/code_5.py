n, pos, l, r = map(int, input().split())

# If all tabs are within the desired range, no action is needed
if l <= pos <= r:
    print(0)
    exit()

# Calculate the number of actions needed
actions = 0

# If we need to close tabs to the left of 'l'
if pos < l:
    actions += l - pos  # Move to 'l'
    actions += 1  # Close all tabs to the left of 'l'

# If we need to close tabs to the right of 'r'
elif pos > r:
    actions += pos - r  # Move to 'r'
    actions += 1  # Close all tabs to the right of 'r'

# If we need to close tabs on both sides
else:
    # Closing left side
    if pos > r:
        actions += pos - r + 1  # Move to 'r' and close
    else:
        actions += l - pos + 1  # Move to 'l' and close

print(actions)