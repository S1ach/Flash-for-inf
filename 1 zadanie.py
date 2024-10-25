f = open('17(1).txt')
t = [int(i) for i in f]
maxim = 0
k = 0

for i in range(len(t)):
    if 32 <= int(oct(t[i])[2:]) <= 64:
        k += 1
        maxim = max(maxim, t[i])
print(maxim, k)


