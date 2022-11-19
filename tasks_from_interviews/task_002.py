
"""
Улучшите этот кусок кода

a = [[1, 2, 3], [11, 12, 13], [21, 22, 23], [31, 32, 33]]
b = [[41, 42, 43], [51, 52, 53], [61, 62, 63], [71, 72, 73]]
summa_a_b = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        summa_a_b[i][j] = a[i][j] + b[i][j]
print(summa_a_b)
"""

a = [
    [1, 2, 3],
    [11, 12, 13],
    [21, 22, 23],
    [31, 32, 33]
]
b = [
    [41, 42, 43],
    [51, 52, 53],
    [61, 62, 63],
    [71, 72, 73]
]
summa_a_b = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]

for i in range(len(a)):
    for j in range(len(a[0])):
        summa_a_b[i][j] = a[i][j] + b[i][j]
print(summa_a_b)


"""
# Улучшите этот кусок кода

spisok = [154,127,98,89,77,55,32,14]  # Пропущены пробелы,  имя переменной 
for i in range(len(spisok)):
   print(i + 1, spisok[i])
"""

lista = [154, 127, 98, 89, 77, 55, 32, 14]

for i in range(len(lista)):
    print(i + 1, lista[i])


"""
Улучшите этот кусок кода

объект resp приходит извне. Это пример.

resp = {"data": ["station1", "station2"], "status_code":200}

if resp["status_code"] == 200:
    station_data = resp["data"]
    for station in station_data:
        if station == "station1":
            if len(station) <= 3:
                print("Hurry up! Bikes are almost out!")
            else:
                print("No need to rush just yet.")
    else:
        print("-!")
        
        
!!! Нарушено выравнивание (if --> else)
"""

resp = {"data": ["station1", "station2"], "status_code": 200}

if resp["status_code"] == 200:
    station_data = resp["data"]
    for station in station_data:
        if station == "station1":
            if len(station) <= 3:
                print("Hurry up! Bikes are almost out!")
            else:
                print("No need to rush just yet.")
        else:
            print("-!")
