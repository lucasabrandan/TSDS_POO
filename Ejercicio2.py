""" 
Ejercicio 2:
Implementar un programa en Python que pida al usuario que ingrese dos números y muestre
la suma, resta, división y multiplicación de ambos.
"""

# Le solicitamos el usuario que ingrese los valores
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Aca realiza las operaciones suma, resta, y multiplicación
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2

# En esta parte se verifica si el numero es diferente a 0, para evitar la división por cero
if numero2 != 0:
    division = numero1 / numero2
else:
    division = "No se puede dividir por cero"

# Mostrar los resultados
print(f"\nSuma: {suma:.2f}")
print(f"Resta: {resta:.2f}")
print(f"Multiplicación: {multiplicacion:.2f}")
print(f"División: {division}")
