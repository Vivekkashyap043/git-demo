# Read input
n = int(input())
rooms = []

for _ in range(n):
    p, q = map(int, input().split())
    rooms.append((p, q))

# Count the number of rooms with free space for both George and Alex
count = sum(1 for p, q in rooms if q - p >= 2)

# Print the result
print(count)
