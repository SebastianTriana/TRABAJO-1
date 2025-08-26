#Autor: Sebastián Triana

#Prueba de novatos

#1 

x = input("Ingrese algo: ")
print(x)

#2
 
print("----------------------")
tabla = int(input("Ingrese un numero: "))
for i in range(1,11):
	print(tabla * i)

#3

print("----------------------")

def factorial(m):    
    n = 1
    for f in range(m, 1, -1):
        n *= f
    return n

m = int(input("Ingrese número objetivo: "))
resultado = factorial(m)
print(f"El factorial de {m} es: {resultado}")



