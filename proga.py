f = open('32.txt')
def ShiftLeft(n: list[int],T: int): #функция циклического сдвига вправо
    x = n.copy()
    for i in range(len(n)):
        x[i] = n[(i+T)%len(n)]
    return x
def ShiftRight(n: list[int],T: int): #циклический сдвиг влево
    x = n.copy()
    for i in range(len(n)):
        x[i] = n[(i-T)%len(n)]
    return x
n = 50 # размер таблицы n на n
T = 5 # на сколько сдвигаем влево или вправо
matrix = [[0 for _ in range(n)] for _ in range(n)] # создаём матрицу nxn
i=0
for s in f: # заполняем её значениями из файла
    k = 0
    for x in s.split():
        matrix[i][k] = int(x)
        k += 1
    i += 1
for prd in range(n): # цикл проходится по главной диагонали и всем, которые ниже
    diag = []
    I = prd
    J = 0
    for i in range(n-prd):
        diag.append(matrix[I][J])
        I += 1
        J += 1
    if prd % 2 == 0:
        diag = ShiftRight(diag,T)
    else:
        diag = ShiftLeft(diag,T)
    I = prd
    J = 0
    for i in range(n-prd): #заполняем матрицу обратно по диагонали
        matrix[I][J] = diag[i]
        I += 1
        J += 1
for prd in range(1,n): # цикл проходится по диагоналям, которые выше главной
    diag = [] # создаём новую диагональ
    I = 0
    J = prd #координаты левой верхней точки
    for i in range(n-prd): #таким образом узнаём длину текущей диагонали
        diag.append(matrix[I][J])
        I += 1
        J += 1 #спускаемся по диагонали

    if prd % 2 == 0: # в нашей матрице четность элементов будет равна prd так как размер диагоналей отличается на 1
        diag = ShiftRight(diag,T)

    else:
        diag = ShiftLeft(diag,T)
    I = 0
    J = prd
    for i in range(n - prd): # заполняем матрицу после сдвига
        matrix[I][J] = diag[i]
        I += 1
        J += 1
a = [sum(matrix[i]) for i in range(len(matrix))] # сумма каждой строки матрицы
print(max(a))
