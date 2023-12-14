k,n,w = map(int,input().split(" "))
total_amount = 0
for i in range(1,w+1):
    total_amount += k * i
if total_amount <= n:
    print("0")
else:
    print(total_amount - n)