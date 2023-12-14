t = int(input())
for _ in range(t):
    st = input()
    if len(st)>10:
        l = st[0]+str(len(st)-2)+st[-1]
    else:
        l = st
    print(l)