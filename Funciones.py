import matplotlib.pyplot as plt
from sympy import symbols, solve, Poly, sympify, lambdify
import re
import numpy as np

print("------Variacion de Funciones-----")
print("Ingresa tu funcion\n")
print("Coloca los caracteres de mayor orden a menor\n")
fin = input("f(x)=")
fi = fin.replace("^", "**")
# Regex para poner * entre numero y letra
f_str = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', fi) 

# Busca la variable en el texto
v = None
try:
    expr = sympify(f_str)
    if expr.free_symbols:
        v = list(expr.free_symbols)[0]
    else:
        v = symbols('x') # Por defecto si es una constante
except:
    print("Error al leer la función.")
    exit()

# Convertimos la cadena para leerla en sympy
p = Poly(expr, v)
#Extrae todos los coeficientes
coeficientes = p.all_coeffs()

# Generamos las potencias originales basándonos en la cantidad de coeficientes
grado_max = len(coeficientes) - 1
potencias = list(range(grado_max, -1, -1)) 

# Calculo de la primer derivada
coeficientesdv = [] #Lista para coeficientes de la derivada
potenciasdv = [] # Lista para las potencias de la derivada

for i in range(len(coeficientes)):
    pot_actual = potencias[i]
    coef_actual = coeficientes[i]
    
    #Valor para nuevos coeficientes
    coefdv = coef_actual * pot_actual
    
    # Si la potencia era 0 (constante), su derivada es 0 y desaparece
    # Si el nuevo coeficiente es 0, tampoco lo guardamos
    if pot_actual > 0: 
        coeficientesdv.append(coefdv)
        potenciasdv.append(pot_actual - 1) # La potencia baja un grado

# Cadena para la derivada a imprimir
fdvs = ""

# Recorremos las listas de coeficientes 
for i in range(len(coeficientesdv)):
    coef = coeficientesdv[i]
    pot = potenciasdv[i] 
    
    if coef == 0:
        continue # Saltamos términos que tengan coeficiente 0

    # Si ya hay algo escrito y el num es positivo, ponemos +
    if len(fdvs) > 0 and coef > 0:
        fdvs += "+"
    
    # Para no imprimir 1x
    if abs(coef) == 1 and pot != 0:
        if coef == -1:
            fdvs += "-"
        # Si es 1, no escribimos nada, solo pasamos a la variable
    else:
        fdvs += str(coef)
    
    # Mientras no sea el termino independiente
    if pot > 0:
        fdvs += str(v)
        if pot > 1:
            fdvs += "^" + str(pot)


if fdvs == "":
    fdvs = "0"
    print("\nTu funcion derivada es: 0")
    exit()


print("\nTu funcion derivada es: ")
print(f"f'(x) = {fdvs}")

#Cambia los ^ por ** que simblizan la potencia para la primer derivada
fdvf = fdvs.replace("^", "**")
#Coloca el simbolo * despues del coeficiente
fdv = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', fdvf) 

#Convertimos la cadena a una ecuacion igualada a 0
d1 = sympify(fdv)
#Nos da los puntos criticos a evaluar en la segunda derivada
raices = solve(d1, v)

print("\nLas raices de tu funcion derivada igualada a 0 son:\n")
print(raices)

# Calculo de la segunda derivada
coeficientesdv2 = [] #Lista para coeficientes de la segunda derivada
potenciasdv2 = [] # Lista para las potencias de la segunda derivada

for i in range(len(coeficientesdv)):
    pot_actual = potenciasdv[i]
    coef_actual = coeficientesdv[i]
    
    #Valor para nuevos coeficientes
    coefdv = coef_actual * pot_actual
    
    # Si la potencia era 0 (constante), su derivada es 0 y desaparece
    # Si el nuevo coeficiente es 0, tampoco lo guardamos
    if pot_actual > 0: 
        coeficientesdv2.append(coefdv)
        potenciasdv2.append(pot_actual - 1) # La potencia baja un grado

# Limpiamos la cadena de derivada para volverla a usar
fdvs = ""

# Recorremos las listas de coeficientes otra vez
for i in range(len(coeficientesdv2)):
    coef = coeficientesdv2[i]
    pot = potenciasdv2[i] 
    
    if coef == 0:
        continue # Saltamos términos que tengan coeficiente 0

    # Si ya hay algo escrito y el num es positivo, ponemos +
    if len(fdvs) > 0 and coef > 0:
        fdvs += "+"
    
    # Para no imprimir 1x
    if abs(coef) == 1 and pot != 0:
        if coef == -1:
            fdvs += "-"
        # Si es 1, no escribimos nada, solo pasamos a la variable
    else:
        fdvs += str(coef)
    
    # Mientras no sea el termino independiente
    if pot > 0:
        fdvs += str(v)
        if pot > 1:
            fdvs += "**" + str(pot)

if fdvs == "":
    fdvs = "0"
    print("\nTu segunda derivada es: 0")
    exit()

print("\nLa segunda derivada de tu funcion es:\n")
print(f"f''(x)= {fdvs}\n")
