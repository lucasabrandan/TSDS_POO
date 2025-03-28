""" 
Ejercicio numero 1:
Escribir un programa en Python que pida al usuario que ingrese las medidas de la base y la altura de un rectángulo y muestre:
1.El perímetro del rectángulo
2.El área del rectángulo 
"""

# Solicitar al usuario que ingrese las medidas
base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))

# Calcular el perímetro y el área
perimetro = 2 * (base + altura)
area = base * altura

# Mostrar los resultados
print(f"\nEl perímetro del rectángulo es: {perimetro:.2f}")
print(f"El área del rectángulo es: {area:.2f}")
