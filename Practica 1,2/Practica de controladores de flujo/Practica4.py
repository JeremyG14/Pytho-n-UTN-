'''Escribe un programa que imprima la tabla de multiplicar del número que
el usuario elija. Usa la sentencia for.'''

num= int(input("Introdusca un numero :"))
for i in range (1,11,+1):
    mul= num*i
    print("La tabla de multiplicacion de ",num,"x",i,"es :",mul)