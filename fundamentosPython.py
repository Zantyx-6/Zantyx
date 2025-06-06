#Sección 1: Variables
#1. Intercambio sin variable auxiliar
#Intercambia los valores de dos variables a y b sin usar una variable extra.
a = 5
b = "hola"
print(f"\nValores iniciales: a = {a}, b = {b}")
a, b = b, a  # Intercambio de valores
print(f"Valores intercambiados: a = {a}, b = {b}")

#2. Suma de cuadrados
#Declara dos variables a = 5, b = 3, y almacena el resultado de a² + b² en una tercera variable c
a = 5
b = 3
c = (a*a)+(b*b)
print("\nEl resultado de 5² + 3² es: ",c)

#3. Conversión de tipos
#Convierte un número entero en string, luego a float y finalmente de nuevo a int. Muestra los resultados.
x = 10
print(f"\nValor de x:{x}, {type(x)}")
x = "10"
print(f"Valor de x:{x}, {type(x)}")
x = 10.0
print(f"Valor de x:{x}, {type(x)}")
x = 10
print(f"Valor de x:{x}, {type(x)}")

#4. Redondeo y formato
#Redondea el número 17.8567 a dos decimales y convierte el resultado en string para imprimirlo como: "Resultado: 17.86"
x = 17.8567
print(f"\nValor Original: {x}")
print(f"Valor Redondeado: {round(x,2)}")

#5. Concatenación de variables
#Declara dos variables nombre y edad, y construye un mensaje como: "Hola, mi nombre es Juan y tengo 25 años."
nombre = "Santiago"
edad = 19
print(f"\nHola mi nombre es {nombre} y tengo {edad} años!")

#6. Cálculo de edad actual
#Usando anio_actual y anio_nacimiento, calcula y muestra la edad actual.
añoNac = int(input("\nDigite su año de nacimiento: "))
añoAct = 2025 #datetime
edad = añoAct-añoNac
print(f"Su edad es: {edad} años")

#7. Cuenta regresiva con variables
print(" ")
for i in range(10, -1, -1):
    print(i, end=" => ")

#8. Valor absoluto sin usar abs()
#Implementa una lógica para obtener el valor absoluto de un número entero sin usar abs().
x = int(input("\nDigite un numero para conseguir el valor absoluto: "))
if x < 0:
    x = x*-1
    print(f"Valor absoluto es: {x}")
else:
    print(f"Valor absoluto es: {x}")

#9. Incremento/decremento según paridad
#Si una variable n es par, suma 1. Si es impar, réstale 1. Imprime el nuevo valor.
x = int(input("\nDigite un numero para verificar si es par o impar: "))
if x % 2 ==0:
    print(f"El numero {x} es par")
    x = x + 1
    print(f"El numero ahora impar: {x}")
else:   
    print(f"El numero {x} es impar")
    x = x - 1
    print(f"El numero ahora par: {x}")

#10. Máximo entre tres números
#Dadas tres variables a, b y c, encuentra y muestra cuál es la mayor sin usar max().
a = int(input("\nDigite un número: "))
b = int(input("Digite otro número: "))
c = int(input("Digite otro número: "))
if a > b and a > c:
    print(f"El número {a} es el mayor.")
elif b > a and b > c:
    print(f"El número {b} es el mayor.")
elif c > a and c > b:
    print(f"El número {c} es el mayor.")
elif a == b and a > c:
    print(f"{a} y {b} son los mayores, mayores que {c}.")
elif a == c and a > b:
    print(f"{a} y {c} son los mayores, mayores que {b}.")
elif b == c and b > a:
    print(f"{b} y {c} son los mayores, mayores que {a}.")
else:
    print("Los tres números son iguales.")

#Sección 2: Operadores Relacionales
#11. Verificación de rango
#Verifica si un número entero x está entre 10 y 100 (inclusive). Imprime el resultado booleano.
x = int(input("\nDigite un numero para verificar el rango: "))
if x >= 10 and x < 101:
    print(f"El numero {x} se encuentra en el Rango!")
else:
    print("Numero fuera de Rango")

#12. Comparación de strings (ignorar mayúsculas)
#Dadas dos cadenas a y b, comprueba si son iguales ignorando mayúsculas/minúsculas.
a = input("\nDigite un texto para comparar: ").lower()
b = input("Digite el segundo texto: ").lower()
if a == b:
    print("Los textos son iguales")
else:
    print("Los textos NO son iguales")

#13. Igualdad entre tres variables
#Verifica si tres variables distintas tienen el mismo valor.
a = int(input("\nDigite un numero: "))
b = int(input("Digite un numero: "))
c = int(input("Digite un numero: "))
if a == b and a == c:
    print("las variables son Iguales")
else:
    print("Las variables NO son iguales")

#14. Presencia en lista
#Declara una lista de números y verifica si un número x está contenido en ella
numeros = [1, 2, 3, 4, 5]
x = int(input("\nDigite un numero para verificar su existencia en la lista: "))
if x in numeros:
    print(f"El numero {x} existe !!!")
else: 
    print("El numero NO existe")

#15. Divisibilidad por 3 y 5
#Dado un número n, determina si es divisible simultáneamente por 3 y 5.
n = int(input("\nDigite un numero para etermina si es divisible simultáneamente por 3 y 5: "))
if n % 3 ==0 and n % 5 ==0:
    print(f"El numero {n} es divisible")
else:
    print("El numero NO es divisible")

#16. Números en orden estricto
#Verifica si tres variables a, b, c están en orden ascendente estricto (a < b < c)
print(" ")
numeros = []
for i in range(3):
    x = int(input("Digite 3 numeros: "))
    numeros.append(x)
copia = numeros.copy()
copia.sort()
print(numeros)
print(copia)
if numeros == copia:
    print("La lista esta ordenada ascendente")
else:
    print("Lista NO ordenanda")

#17. Comparación doble
#Dado un número x, y dos límites a y b, verifica si x está estrictamente entre a y b.
a = int(input("\nDigite un numero de inicio: "))
b = int(input("Digite un numero final: "))
x = int(input("Digite un numero para verificar el rango: "))
if x >= a and x < b:
    print(f"El numero {x} se encuentra en el Rango!")
else:
    print("Numero fuera de Rango")

#18. Relación proporcional
#Verifica si una variable a es exactamente el doble de otra variable b
a = int(input("\nDigite un numero normal: "))
b = int(input("Digite un numero doble: ")); c=a
a = a + a
if a == b:
    print(f"El numero {c} es el doble de {b}")
else:
    print(f"El numero {c} NO es el doble de {b}")

#19. Cambio de signo si negativo
#Si una variable x es negativa, conviértela en positiva. Si ya es positiva, déjala igual
x = int(input("\nDigite un numero para convertir en positivo: "))
if x < 0:
    x = x*-1
    print(f"Valor positivo: {x}")
elif x == 0:
    print("Digitaste 0")
else:
    print(f"El valor ya es positivo: {x}")

#20. Detección de tipo
#Dada una variable x, imprime si es un entero (int), flotante (float) o cadena (str).
x = 1.0
if type(x) == str:
    print("\nEl valor es string")
elif type(x) == int:
    print("\nEl valor es int")
elif type(x) == float:
    print("\nEl valor es float")

#Sección 3: Operadores Lógicos (21–30)
#21. ¿Puede votar?
# Verifica si una persona puede votar. Debe tener al menos 18 años y tener documento de identidad (True o False).
x = int(input("\nDigite su edad"))
doc = input("Tienes documento? (s/n)").lower()
if doc == "s":
    if x >= 18:
        print("Usted puede Votar")
    else:
        print("Usted no puede Votar")
else:
    print("Usted no puede Votar sin documento")

#22. Control de acceso lógico Una persona puede entrar si:
#Tiene pase VIP, o Paga entrada y no está ebria. Evalúa esto con tres variables booleanas
pase_vip = input("\n¿Tiene pase VIP? (s/n): ").lower() == 's'
paga_entrada = input("¿Pago la entrada? (s/n): ").lower() == 's'
ebria = input("¿Está ebria? (s/n): ").lower() == 's'
if pase_vip or (paga_entrada and not ebria):
    print("Puede entrar")
else:
    print("No puede entrar")

#23. Validación XOR
#Dadas dos condiciones booleanas cond1 y cond2, verifica si exactamente una es verdadera (operación XOR lógica).
cond1 = input("\nDigite la primera condicion (True/False): ").lower() == 'true'
cond2 = input("Digite la segunda condicion (True/False): ").lower() == 'true'
if (cond1 and not cond2) or (not cond1 and cond2):
    print("Una de las condiciones es verdadera")
else:   
    print("Ambas condiciones son verdaderas o ambas son falsas")

#24. Validación compuesta múltiple
#Dado un número n, verifica si es mayor que 0 y (múltiplo de 2 o de 3)
n = int(input("\nDigite un numero para verificar si es mayor que 0 y multiplo de 2 o 3: "))
if n > 0 and (n % 2 == 0 or n % 3 == 0):
    print(f"El numero {n} es mayor que 0 y multiplo de 2 o 3")
else:
    print(f"El numero {n} NO es mayor que 0 o NO es multiplo de 2 o 3")

#25. Condición contradictoria
#Escribe una condición lógica que nunca se cumple (una contradicción), como x > 5 and x < 1.
x = int(input("\nDigite un numero para verificar una contradiccion: "))
if x > 5 and x < 1:
    print(f"El numero {x} es mayor que 5 y menor que 1")
else:
    print(f"El numero {x} NO es mayor que 5 y menor que 1")

#26. Negación lógica
#Dada una condición x > 10, reescríbela usando not para que tenga el mismo efecto lógico.
x = int(input("\nDigite un numero para verificar si es mayor que 10: "))
if not (x <= 10):
    print(f"El numero {x} es mayor que 10")
else:
    print(f"El numero {x} NO es mayor que 10")

#27. Aprobación de estudiante
#Verifica si un estudiante aprueba: nota >= 3.0 y asistencia >= 80.
nota = float(input("\nDigite la nota del estudiante: "))
asist= int(input("Digite el porcentaje de asistencia del estudiante: "))
if nota >= 3.0 and asist >= 80:
    print("El estudiante aprueba")
else:
    print("El estudiante NO aprueba :(")

#28. Simulación de alarma
#Si la temperatura es menor a 0 o mayor a 38 y la humedad es mayor a 80%, se activa una alarma.
temp = float(input("\nDigite la temperatura actual: "))
humedad = float(input("Digite el porcentaje de humedad: "))
if (temp < 0 or temp > 38) and humedad > 80:
    print("¡Alarma activada: Condiciones extremas detectadas !")
else:
    print("Condiciones normales, alarma desactivada.")

#29. Contraseña segura Verifica si una contraseña cumple con:
#Longitud mayor a 8 caracteres, Contiene al menos un número (Pista: puedes usar any(char.isdigit() for char in passw))
password = input("\nDigite una contraseña segura: ")
if len(password) > 8 and any(char.isdigit() for char in password):
    print("Contraseña segura")
else:
    print("Contraseña insegura, debe tener más de 8 caracteres y al menos un número!!")

#30. Doble negación lógica
#Evalúa una expresión como: "No es falso que no tenga acceso" usando operadores lógicos. Traduce eso a Python.
acceso = input("\n¿Tiene acceso? (s/n): ").lower() == 's'
if not not acceso:
    print("Tiene acceso")
else:
    print("No tiene acceso")
 