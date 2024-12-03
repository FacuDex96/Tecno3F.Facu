#Realizar un programa que le pida al usuario su nombre y edad, y nos diga si es mayor de edad

nombre = "Facundo "
edad = "28"

string = input ("Ingrese su nombre: ")
string = int (input ("Ingrese su edad: "))

if edad > 18:
   print ("Es mayor de edad")
else: 
    print ("Es menor de edad")