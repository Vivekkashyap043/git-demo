n = int(input())
numberOfPeople = 0
capacity = []
for i in range(n):
    a, b = map(int, input().split())
    numberOfPeople = (numberOfPeople - a) + b
    capacity.append(numberOfPeople)
print(max(capacity))   
    