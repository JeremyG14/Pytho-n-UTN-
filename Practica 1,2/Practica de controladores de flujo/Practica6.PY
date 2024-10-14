'''Escribe un programa que le pida al usuario ingresar tres números enteros
y muestre cuál es el mayor. Usa operadores lógicos para verificar si
todos los números son diferentes o si algunos son iguales.'''
num1 = int(input("Ingrese un numero :"))
num2 = int(input("Ingrese un numero :"))
num3 = int(input("Ingrese un numero :"))

if num1!=num2 and num2!=num3   and  num1!=num3:
    print("Todos los numeros son iguales")
else:
    print("No todos los numero son iguales vuelva a ingresarlos ")
if num1>num2 and num1>num2:
    mayor=num1
    
elif num2<num1 and num2>num3:
    mayor=num2
else:
    mayor=num3

print("El numero mayor es : ",mayor)









