def sum_of_number(n):
    return sum(int(i) for i in str(n))

f = open('17(3).txt')
t = [int(i) for i in f]
k = sorted(t)
count = 0

if len(k) % 2 == 0:
    mediana = ((k[len(k)//2] + k[len(k)//2 - 1]) // 2)
else:
    mediana = k[len(k)//2]

for i in range(len(t)):
    if sum_of_number(t[i]) > sum_of_number(mediana):
        count += 1

print(mediana, count)

