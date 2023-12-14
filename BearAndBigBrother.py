a,b = map(int, input().split())
year = 0
tempa = a
tempb = b
while True:
    tempa *= 3
    tempb *= 2 
    year += 1
    if tempa > tempb:
        break
print(year)