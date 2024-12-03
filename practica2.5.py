#Realizar un programa que sume los numeros ingresados por el usuario hasta que se ingrese un 0. Al finalizar nos debe mostrar la suma por pantalla

numero = 1
suma_total = 0

while numero != 0:
    numero = float(input("Ingrese un numero: "))
    suma_total += numero
    
print(f"La suma total es: {suma_total}")
