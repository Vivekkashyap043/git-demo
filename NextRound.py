# Read input values
n, k = map(int, input().split())
scores = list(map(int, input().split()))

# Find the score of the k-th participant
kth_score = scores[k - 1]

# Count the number of participants who advance to the next round
advancers = sum(1 for score in scores if score >= kth_score and score > 0)

# Output the result
print(advancers)
