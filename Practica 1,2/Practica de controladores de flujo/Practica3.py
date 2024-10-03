'''Escribe un programa que solicite al usuario un número entero positivo e
imprima todos los números desde 1 hasta ese número.
o Variante: Haz que el programa también sume todos los números
impresos y muestre el total al final.'''

suma=0
num=int (input("Ingrese un numero entero positivo :"))
while num<0:
    print("Ingrese un numero negativo")
    print("Ingrese un  numero positivo :")

for i in range (1,num,+1):
    print("Numero :",i)
    suma=suma+i
print( "La suma de los numeros son :",suma)
