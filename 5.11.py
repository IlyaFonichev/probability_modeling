import random


repeats = 1000
counter = 0
print("Отклонение центра первой окружности относительно центра первой полосы")
for i in range(repeats):
    deflection = int(random.random() * 120) - 60
    if (abs(deflection) - 15 <= 0) or (deflection >= 30):
        counter += 1
    print(deflection)
print("Вероятность, что хотя бы одна из окружностей пересечет полосу: " + str(counter / repeats))
