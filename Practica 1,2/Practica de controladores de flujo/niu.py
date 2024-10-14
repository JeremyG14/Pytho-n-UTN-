# Solicitar tres números enteros al usuario
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))

# Verificar si todos los números son diferentes
if num1 != num2 and num1 != num3 and num2 != num3:
    print("Todos los números son diferentes.")
else:
    print("Algunos números son iguales.")

# Determinar el número mayor
if num1 >= num2 and num1 >= num3:
    mayor = num1
elif num2 >= num1 and num2 >= num3:
    mayor = num2
else:
    mayor = num3

# Mostrar el número mayor
print(f"El número mayor es: {mayor}")
