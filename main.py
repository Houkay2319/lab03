N = int(input("Введите размерность массива: "))
a = []
for i in range(N):
    a.append(int(input()))
print(a)

for i in range(N - 1):
    for j in range(N - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

N = int(input("Если вы хотите сортировку в прямом порядке введите 0, в обратном 1: "))
if(N == 0):
    print(a)
else:
    a.reverse()
    print(a)