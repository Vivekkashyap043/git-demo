n = int(input())
names = input()
if names.count("A") > names.count("D"):
    print("Anton")
elif names.count("A") < names.count("D"):
    print("Danik")
else:
    print("Friendship")