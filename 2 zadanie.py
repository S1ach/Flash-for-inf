f = open('17(2).txt')
t = [int(i) for i in f]
minimum1 = 10**10
minimum2 = 10**10

for i in range(2, len(t), 3):
    if abs(t[i]) % 10 >= 4:
        minimum1 = min(minimum1, t[i])

for j in range(2, len(t), 3):
    if abs(t[j]) % 10 >= 4 and t[j] != minimum1:
        minimum2 = min(minimum2, t[j])

minimum_sum = minimum1 + minimum2
odnerki = str(bin(minimum_sum)[3:]).count("1")
print(abs(minimum_sum), odnerki)


