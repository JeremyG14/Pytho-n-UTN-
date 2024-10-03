'''Diseña un programa que tome dos números enteros del usuario y
muestre:
▪ La suma.
▪ La resta.
▪ La multiplicación.
▪ La división (ten en cuenta que uno puede ser 0, verifica esto antes
de dividir).
▪ El módulo (resto de la división).'''
num1=int(input("Ingrese un numero entero :"))
num2=int(input("Ingrese un numero entero :"))
suma=num1+num2
print("La suma de",num1,"y",num2,"es :",suma)
resta=num1-num2
print("la resta de ",num1,"y",num2,"es :",resta)
mul=num1*num2
print("la multiplicacion de ",num1,"y",num2,"es :",mul)
if num2!=0:
    div=num1/num2
    print("la divicion de ",num1,"y",num2,"es :",div)
else:
    print("No se puede dividir entre 0.")

if num2!=0:
    modulo=num1 % num2
    print("El modulo de ",num1,"entre",num2,"es :",modulo)
else:
    print("No se puede dividir entre 0.")