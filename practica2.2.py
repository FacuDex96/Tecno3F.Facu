#Realizar un programa que genere la tabla de multiplicar de un numero ingresado por el usuario (del 1 al 10)

numero = int(input("Ingrese un numero: "))

for i in range (1, 11):
    print(f"[i] x [numero] = [i x numero]")