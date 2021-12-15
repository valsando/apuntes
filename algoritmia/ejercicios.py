print("respestas a los ejercicios:")
N = int(input("ingrese el numero del ejercicio: "))
while 1 <= N <= 20:
    if N == 1:
        a = 10
        b = 20
        c = 10
        a = a + 15
        b = b + 12
        c = a * c
        print(f"a = {a}, b = {b}, c= {c}")
        N = int(input("algun otro?"))
    elif N == 2:
        a = 3
        b = 8
        c = 1
        a = 5
        b = 9
        c = 7
        a = a + 1
        b = b + 2
        c = c + 3
        print(f"a = {a}, b = {b}, c= {c}")
        N = int(input("algun otro?"))
    elif N == 3:
        a = 10
        b = 5
        c = 10
        a = a + b - 5
        b = a + b - 5
        c = a + b - 5
        a = a + 5 * b / 2
        b = a + 5 * b / 2
        c = a + 5 * b / 2
        print(f"a = {a}, b = {b}, c= {c}")
        N = int(input("algun otro?"))
    elif N == 4:
        a = 5
        b = 5
        c = 5
        a = a + a
        b = b + b
        c = c + c
        a = a + b + c
        b = a + b + c
        c = a + b + c
        print(f"a = {a}, b = {b}, c= {c}")
        N = int(input("algun otro?"))
    elif N == 5:
        a = 10
        b = 10
        c = 10
        a = a + 5
        b = a + 3
        c = a + 2
        a = b + 4
        b = b + 5
        c = c + 8
        print(f"a = {a}, b = {b}, c= {c}")
        N = int(input("algun otro?"))
    elif N == 6:
        a = 10
        b = 1
        c = 4
        a = a + c
        b = a + c
        c = a + c
        a = c + 5
        b = c + b
        c = a + b + c
        print(f"a = {a}, b = {b}, c= {c}")
        N = int(input("algun otro?"))
    elif N == 7:
        a = 1
        b = 1
        c = 1
        a = a + a
        b = b + a
        c = c + a
        a = a + a
        b = b + a
        c = c + a
        print(f"a = {a}, b = {b}, c= {c}")
        N = int(input("algun otro?"))
    elif N == 8:
        a = 10
        b = 50
        c = 30
        a = a - b
        b = b - c
        c = c - a
        a = a - 1
        b = b - a
        c = c + a - b
        print(f"a = {a}, b = {b}, c= {c}")
        N = int(input("algun otro?"))
    elif N == 9:
        a = 1
        b = 2
        c = 3
        a = a + b
        b = a - b
        c = a * b
        a = a - b
        b = a + b
        c = a * b
        print(f"a = {a}, b = {b}, c= {c}")
        N = int(input("algun otro?"))
    elif N == 10:
        a = 1
        b = 2
        c = 3
        a = a + 2
        b = a + 2 + b
        c = a + 2 + c
        a = a / 2
        b = b / 2
        c = c / 2
        print(f"a = {a}, b = {b}, c= {c}")
        N = int(input("algun otro?"))
    elif N == 11:
        print("x= (a + b / c) / ((a / b) + c)")
        N = int(input("algun otro?"))
    elif N == 12:
        print("x= (a + b + a / b) / c")
        N = int(input("algun otro?"))
    elif N == 13:
        print("x= (a / (a + b)) / ((a / (a - b) ")
        N = int(input("algun otro?"))
    elif N == 14:
        print("x= (a / (b / (a + b + b / c)) / (a + b / (a + c))")
        N = int(input("algun otro?"))
    elif N == 15:
        print("x= (a + b + c) /  (a + b / c )")
        N = int(input("algun otro?"))
    elif N == 16:
        print("x= (a + b + c / (d * a)) / (a + b * c / d)")
        N = int(input("algun otro?"))
    elif N == 17:
        print("x= (a + b / c + d) / a")
        N = int(input("algun otro?"))
    elif N == 18:
        print("x= ((a / b) + (b / c)) / ((a / b) - (b / c))")
        N = int(input("algun otro?"))
    elif N == 19:
        print("x= a + (a + (a + b) / (c + d)) / (a + (a / b))")
        N = int(input("algun otro?"))
    elif N == 20:
        print("x= a + b + c / d + (a / (b - c)) / (a / (b + c))")
        N = int(input("algun otro?"))
print("no es un valor esperado, hasta la proxima :)")
