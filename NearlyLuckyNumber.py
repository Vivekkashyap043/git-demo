def count_lucky_digits(number):
    count = 0
    while number > 0:
        digit = number % 10
        if digit == 4 or digit == 7:
            count += 1
        number //= 10
    return count
def is_lucky_number(num):
    return num == 4 or num == 7 or num == 44 or num == 47 or num == 74 or num == 77
def is_nearly_lucky_number(n):
    lucky_digit_count = count_lucky_digits(n)
    return is_lucky_number(lucky_digit_count)
n = int(input().strip())
if is_nearly_lucky_number(n):
    print("YES")
else:
    print("NO")
