#Escribe una expresión que devuelva True si x es mayor que 10 y menor que 20.
x = int(input("Ingrese un numero: "))
res = x > 10 and x < 20
print(f"El resultado de la expresion es: {res}")

#Escribe una condición que devuelva True si a es igual a b o c es mayor que 100.
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
c = int(input("Ingrese el valor de c: "))
res = a == b or c > 100
print(f"El resultado de la condicion es: {res}")

#¿Qué devuelve esta expresión y por qué? True or False and False
res = True or False and False
print(f"El resultado de la expresion 'True or False and False' es: {res}")

#¿Qué resultado tiene la siguiente operación? (5 > 3) ^ (2 < 1)
res = (5 > 3) ^ (2 < 1)
print(f"El resultado de la operacion '(5 > 3) ^ (2 < 1)' es: {res}")

#Reescribe la siguiente expresión usando operadores relacionales y lógicos: not (a < b or b < c)
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
c = int(input("Ingrese el valor de c: "))
res = not (a < b or b < c)
print(f"El resultado de la expresion 'not (a < b or b < c)' es: {res}")

#Dado x = 10, y = 20, escribe una condición que devuelva True solo si x y y son diferentes y al menos uno de los dos es mayor que 15.
x = 10
y = 20
res = (x != y) and (x > 15 or y > 15)
print(f"El resultado de la condicion es: {res}")

#Evalúa el resultado de: (10 != 5) and (4 == 4) or (2 > 3)
x = 10
y = 5
z = 4
res = (x != y) and (z == z) or (2 > 3)
print(f"El resultado de la expresion '(10 != 5) and (4 == 4) or (2 > 3)' es: {res}")

#Dado el siguiente código, ¿cuál es el valor de resultado? a = True b = False resultado = a ^ b
a = True
b = False
res = a ^ b
print(f"El valor de resultado es: {res}")

#¿Qué devuelve esta expresión en Python y por qué? (3 > 2) and (2 > 1) ^ False
x = 3
y = 2
z = 1
res = (x > y) and (y > z) ^ False
print(f"El resultado de la expresion '(3 > 2) and (2 > 1) ^ False' es: {res}")   #Es True porque (3 > 2) es True, (2 > 1) es True, y True and True es True. Luego, True ^ False es True.

#Escribe un programa que reciba dos números y diga si exactamente uno de ellos es positivo (usa xor para resolverlo).
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
res = (num1 > 0) ^ (num2 > 0)
print(f"El resultado de la condicion es: {res}")


