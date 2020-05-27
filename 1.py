import matplotlib.pyplot as plt
import random

def Func():
    global BUF
    global N
    global ListOfProbability
    global AverageOfT
    global p

    while p <= 1/N:
        query = list()
        m = 0
        ListOfProbability.append(p)
        while m <= BUF:
            SumOfAb = 0
            n = 0
            while n <= N:
                SumOfAb += random.choices([1, 0], [p, 1 - p])[0]
                n += 1
            if len(query) == 0: query.append(0)
            if query[-1] <= 0: query.append(SumOfAb)
            if query[-1] > 0:
                result = int(query[-1] - 1 + SumOfAb)
                query.append(result)
            m += 1
        SumOfQuery = sum(query)
        if p == 0: AverageOfT.append(0)
        if p != 0:
            result = int(SumOfQuery/p)
            AverageOfT.append(result)
        p += 0.01

    plt.xlabel("Вероятность попадания в буфер")
    plt.ylabel("Среднее время ожидания")
    plt.title('При кол-ве абонентов ' + str(N))
    plt.plot(ListOfProbability, AverageOfT)
    plt.show()

BUF = 1000                  #размер буфера
N = int(input("Сколько абонентов=? "))  #число абонентов
p = 0                       #вероятность
ListOfProbability = list()  #массив вероятности
AverageOfT = list()         #среднее
Func()                      #вызов функции