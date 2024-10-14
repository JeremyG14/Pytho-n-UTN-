'''Crea un programa que pida al usuario su edad y si tiene licencia de
conducir (sí/no). El programa debe indicar si puede alquilar un coche,
sabiendo que:
▪ Debe tener al menos 21 años.
▪ Debe tener una licencia de conducir válida.'''
edad=int(input("Ingrese su edad :"))
licencia =(input("Usted tiene licencia de conducir valida Si/No :"))
if edad>=21 and  licencia == "si":
    print("Usted si puede alquilar un auto")
else:
    print("Usted no puede alquilar un auto")
