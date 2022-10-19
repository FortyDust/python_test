n = int(input())
for i in range(1, (n//2)+2):
    for j in range(i):
        print('*', end='')
    print()
for a in range(n // 2, 0, -1):
    for b in range(a):
        print('*', end='')
    print()