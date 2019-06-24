def task_one():
    a = int(input("first number "))
    b = int(input("second number "))
    print("Произведение = ", a * b, "\n", "Сумма = ", a + b)

task_one()


def task_two():
    a = int(input("number "))
    print("Квадрат числа = ", a**2, "Куб числа = ", a**3)

task_two()


def task_three():
    a = int(input("first number "))
    b = int(input("second number "))
    c = int (input("third number "))
    print ("Сумма вычислений = ", (a*2)+(b-3)+(c**2))

task_three ()


def task_four ():
    a = int(input("first number "))
    b = int(input("second number "))
    c = int(input("third number "))
    print("Среднее ", (a+b+c)/3, "\n", "Разность... ", (a+c)*2-b*3)

task_four()


def task_five():
    a = int(input("print the square side lengh = "))
    print("Периметр = ", a*4, "\n", "Площадь = ", a*a)

task_five()


def task_six():
    a = float(input("price of biscuits = "))
    b = float(input("price of candies = "))
    print("a) ", round(b*0.3+a*0.4,2), "\n", "b) ", round((a*2+b*1.8)*3,2))

task_six()


def task_seven():
    a = float(input("time, min = "))
    b = float(input("distance, km = "))
    print("Скорость в м/с = ", round((b*1000)/(a*60),2))

task_seven()


def task_eight():
    import math
    a = float(input("cated a = "))
    b = float(input("cated b = "))
    print("S = ", a*b/2, "\n", "P = ", a+b+math.sqrt(a**2+b**2), "\n", "c = ", math.sqrt(a**2+b**2))

task_eight()


def task_nine():
    a = float(input("C = "))
    print("F = ", a*(9/5)+32)

task_nine()
