cont= 0
suma= 0
while cont < 15:
    print(cont)
    suma = suma + cont
    if cont == 3:
        break
    cont = cont + 1
print("La suma es:", suma)