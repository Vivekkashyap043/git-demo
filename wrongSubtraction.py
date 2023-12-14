def tanya_subtract(n, k):
    for _ in range(k):
        if n % 10 != 0:
            n -= 1
        else:
            n //= 10

    print(n)

# Example usage:
input_values = input().split()
n = int(input_values[0])
k = int(input_values[1])
tanya_subtract(n, k)
