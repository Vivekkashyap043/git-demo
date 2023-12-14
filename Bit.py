t = int(input())
count = 0
for i in range(t):
    s = input()
    if s == "++X" or s == "X++":
        count += 1
    else:
        count -= 1    
        
print(count)    


def hello():
    print("ok")
