# Function to check if one of the numbers is the sum of the other two
def check_sum(a, b, c):
    return a + b == c or a + c == b or b + c == a

# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    # Read the three integers a, b, c for each test case
    a, b, c = map(int, input().split())

    # Check and print the result for each test case
    if check_sum(a, b, c):
        print("YES")
    else:
        print("NO")
