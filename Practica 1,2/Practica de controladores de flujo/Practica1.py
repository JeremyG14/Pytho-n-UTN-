'''Crea un programa que solicite la edad de una persona e indique si es
mayor de edad (18 años o más) o no.
o Variante: Modifica el programa para que además indique si es un
adolescente (entre 13 y 17 años).'''
edad = int(input("Ingrese su edad  :"))
if edad >=18:
    print("Usted es mayor de edad")
elif edad>=13 and edad<=17:
    print("Usted tiene la edad entre 13 y 17 años")
else:
    print("Usted es menor de edad")