length = 6

L = ['Антон', 'Вася', 'Женя', 'Валя', 'трактор', 'Таня']

print(L)

for i in range(length-1):
    for j in range(length-i-1):
        if L[j] > L[j+1]:
            temp = L[j]
            L[j] = L[j+1]
            L[j+1] = temp

print(L)