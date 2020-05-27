import matplotlib.pyplot as plt
import random

def Func():
    global BUF
    global N
    global ListOfProbability
    global AverageOfT
    global p

    while p <= 1/N:
        m = 0
        SUmOfCollision = 0
        SumOfSumAb = 0
        ListOfProbability.append(p)
        while m <= BUF:
            SumOfAb = 0
            n = 0
            while n <= N:
                SumOfAb += random.choices([1, 0], [p, 1 - p])[0]
                n += 1
            if SumOfAb > 1:
                SUmOfCollision += SumOfAb
            SumOfSumAb += SumOfAb
            m += 1
        result = float(SUmOfCollision/SumOfSumAb)
        AverageOfT.append(result)
        p += 0.005

    plt.xlabel("Вероятность попадания в буфер")
    plt.ylabel("Среднее время ожидания")
    plt.title('При кол-ве абонентов ' + str(N))
    plt.plot(ListOfProbability, AverageOfT)
    plt.show()


BUF = 1000                  #размер буфера
N = int(input("Сколько абонентов=? "))  #число абонентов
p = 0.0005                       #вероятность
ListOfProbability = list()  #массив вероятности
AverageOfT = list()         #среднее
Func()                      #вызов функции