count = 0
for i in range(1001,10000):
    if count == 3:
        break
    a = int(str(i)[0]) + int(str(i)[-1]) #сумма крайних цифр
    b = sum([int(x) for x in str(i)]) - a # cумма средних (всех, кроме крайних цифр)
    if b%8 - a%8 == 2:
        print(i)
        count += 1