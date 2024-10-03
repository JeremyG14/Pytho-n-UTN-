'''Crea un programa que le pida al usuario ingresar dos números enteros y
un número flotante. Luego muestra la suma de los dos enteros y el
producto del entero con el flotante.'''
num1=int(input("Ingrese un numero entero :"))
num2=int(input("Ingrese un numero entero :"))
num1f=float(input("Ingrese un numero flotante :"))
suma=num1+num2
print("La suma de",num1,"y",num2,"es :",suma)
mul=suma*num1f
print("la multiplicacion de ",suma,"y",num1f,"es :",mul)