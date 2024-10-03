'''Escribe un programa que le pida al usuario ingresar su nota en una
prueba (un número entre 0 y 10). El programa debe mostrar:
▪ "Insuficiente" si la nota es menor que 4.
▪ "Regular" si la nota es mayor o igual a 4 pero menor que 6.
▪ "Bueno" si la nota es mayor o igual a 6 pero menor que 8.
▪ "Muy Bueno" si la nota es mayor o igual a 8 pero menor que 10.
▪ "Excelente" si la nota es igual a 10.'''
nota=0
while nota<=0 or nota>10:
    nota=float(input("Ingrese su nota :"))
    if nota < 0 or nota > 10:
        print("Nota no valida")

if nota < 4:
    print("Insuficiente")
elif nota >= 4 and nota < 6:
    print("Regular")
elif nota >= 6 and nota < 8:
    print("Bueno")
elif nota >= 8 and nota < 10:
    print("Muy Bueno")
elif nota == 10:
    print("Excelente")
