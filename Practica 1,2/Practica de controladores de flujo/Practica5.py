'''Crea un programa que solicite al usuario una contraseña (puedes definir
una tú). El programa debe pedir la contraseña hasta que el usuario la
escriba correctamente.'''
contraseña=(input("Introdusca una contraseña :"))
can="Jeremy"
while can != contraseña:
    print("La contraseña es incorrecta")
    contraseña=(input("Vuelva a introducir una nueva contraseña :"))
