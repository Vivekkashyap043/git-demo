# Read input
n, t = map(int, input().split())
initial_arrangement = list(input())

# Process the arrangement after t seconds
for _ in range(t):
    i = 0
    while i < n - 1:
        if initial_arrangement[i] == 'B' and initial_arrangement[i + 1] == 'G':
            # Swap the positions of a boy and a girl
            initial_arrangement[i], initial_arrangement[i + 1] = initial_arrangement[i + 1], initial_arrangement[i]
            i += 2  # Skip the next position as it is a boy
        else:
            i += 1

# Print the result
print(''.join(initial_arrangement))
