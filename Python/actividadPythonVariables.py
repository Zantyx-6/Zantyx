#Ejercicio 1: Suma de dos números
#Descripción: Pide dos números al usuario, almacénalos en variables y muestra su suma.
x = 10
y = 5
print(f"La suma de {x} con {y} es igual a = {x+y}")

#Ejercicio 2: Conversión de grados Celsius a Fahrenheit
#Fórmula: F = C * 1.8 + 32
celsius = 20
fahrenheit = celsius * 1.8 + 32
print(f"\n{celsius} °C a Fahrenheit es: {fahrenheit}")

#Ejercicio 3: Área de un triángulo
#Fórmula: Área = (base * altura) / 2
base = 8
altura = 6
area = (base * altura) / 2
print(f"\nSe tiene una base de {base}cm y una altura de {altura}cm, el area del triangulo es: {area}cm² ")

#Ejercicio 4: Par o impar
#Descripción: Pide un número y determina si es par o impar usando if
x = int(input("\nDigite un numero para verificar si es par o impar: "))
if x % 2 ==0:
    print(f"El numero {x} es par")
else:   
    print(f"El numero {x} es impar")

#Ejercicio 5: Intercambiar valores entre dos variables
#Descripción: Intercambia los valores de dos variables sin usar una tercera variable.
a = 5
b = "hola"
print(f"\nValores iniciales: a = {a}, b = {b}")
a, b = b, a  # Intercambio de valores
print(f"Valores intercambiados: a = {a}, b = {b}")

#Ejercicio 6: Calculadora simple
#Descripción: Realiza suma, resta, multiplicación y división con dos números ingresados por el usuario
print("\nCalculadora:")
x = int(input("Digite un numero: "))
y = int(input("Digite otro numero: "))
print(f"Suma de los numeros digitados: {x+y}")
print(f"Resta de los numeros digitados: {x-y}")
print(f"Multiplicación de los numeros digitados: {x*y}")
print(f"División de los numeros digitados: {x/y}")

#Ejercicio 7: Edad en años, meses y días
#Descripción: A partir de la edad en años, calcula la cantidad aproximada de meses y días.
edad = int(input("\nDigite su edad: "))
print(f"Su edad {edad} en meses es: {edad*12} meses")
print(f"Su edad {edad} en dias es: {edad*365} meses")

#Ejercicio 8: Número mayor
#Descripción: Pide tres números al usuario y muestra cuál es el mayor
a = int(input("\nDigite un numero: "))
b = int(input("Digite un numero: "))
c = int(input("Digite un numero: "))
if a>b & a>c:
    print(f"El numero {a} es mayor que {b} y {c}")
elif b>a & b>c:
    print(f"El numero {b} es mayor que {a} y {c}")
elif c>a & c>b:
    print(f"El numero {c} es mayor que {a} y {b}")
else:
    print("Los numeros son iguales")

#Ejercicio 9: Verificar si un número es múltiplo de otro
#Descripción: Pide dos números y determina si el primero es múltiplo del segundo.
x = int(input("\nDigite un numero: "))
y = int(input("Digite otro numero: "))
if x % y == 0:
    print(f"El numero {x} es multiplo de {y}")
else:
    print(f"El numero {x} no es multiplo de {y}")

#Ejercicio 10: Salario con bonificación
#Descripción: Calcula el salario total si un empleado recibe un bono del 10% sobre su salario base.
S_base = float(input("\nDigite su salario base: "))
bono = S_base * 0.10
salario_T = S_base + bono
print(f"Su salario base es: {S_base} y su bono es: {bono}, por lo tanto su salario total es: {salario_T}")
