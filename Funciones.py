import matplotlib.pyplot as plt
from sympy import symbols, solve, Poly, sympify, lambdify
import re
import numpy as np

print("------Variacion de Funciones-----")
print("\nIngresa tu funcion")
print("Coloca los caracteres de mayor orden a menor (Ej 3x^2 - 2x + 6) \n")
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

#Colocamos formato para que pueda operar python
#Cambia los ^ por ** que simblizan la potencia para la primer derivada
fdvc = fdvs.replace("^", "**")
#Coloca el simbolo * despues del coeficiente
fdv2 = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', fdvc)

#Convertimos la funcion a sympify
d2 = sympify(fdv2)

#Arreglos para guardar valores
xmaximos = []
xminimos = []
#Evaluamos los puntos obtenidos para saber si son maximos o minimos
for raiz in raices:
    #Para saltar soluciones imaginarias ya que no se pueden graficar con las demas
    if not raiz.is_real:
        continue
    result = d2.subs(v, raiz)
    if result < 0:
        xmaximos.append(raiz)
    if result > 0:
        xminimos.append(raiz)

print("Los puntos maximos de tu funcion son: \n")
print(xmaximos)
print("\nLos puntos minimos de tu funcion son: \n")
print(xminimos)

#Guardamos los puntos maximos y minimos con su termino en y

ymaximos = []
yminimos = []

#Evaluamos en los puntos maximos
for valor_x in xmaximos:
    y = expr.subs(v, valor_x)
    ymaximos.append(y)

#Evaluamos en los puntos minimos
for valor_x in xminimos:
    y = expr.subs(v, valor_x)
    yminimos.append(y)

print("Evaluamos los puntos maximos y minimos en la funcion original\n")

if len(xmaximos) > 0:
    print("\nLos puntos maximos son:\n")
    for x, y in zip(xmaximos, ymaximos):
        print(f"Coordenada: ({x.evalf(2)}, {y.evalf(2)})")
else:
    print("\nNo se encontraron puntos máximos.")

if len(xminimos) > 0:
    print("\nLos puntos minimos son:\n")
    for x, y in zip(xminimos, yminimos):
        print(f"Coordenada: ({x.evalf(2)}, {y.evalf(2)})")
else:

    print("\nNo se encontraron puntos mínimos.")

# ----graficas----
#Graficamos los puntos y trazamos la funcion

#Convierte la funcion a una forma mas agil de uso
f_numerica = lambdify(v, expr, modules=['numpy'])

#Guardamos todos los puntos criticos juntos
puntos_criticos_x = xmaximos + xminimos

if len(puntos_criticos_x) > 0:
    # Convertimos a float para que no salgan numeros raros y para matplot
    vals_float = [float(sympify(val).evalf()) for val in puntos_criticos_x]
    min_x = min(vals_float)
    max_x = max(vals_float)
    
    # Agregamos un margen del 30% a los lados
    margen = (max_x - min_x) * 0.3
    if margen == 0: margen = 2
    
    lim_izq = min_x - margen
    lim_der = max_x + margen

# Cambiamos el formato de cadena para agilizar la obtencion de datos
f_numerica = lambdify(v, expr, modules=['numpy'])
x_vals = np.linspace(lim_izq, lim_der, 500)
y_vals = f_numerica(x_vals)

# Ancho y Alto de la ventana de grafica
plt.figure(figsize=(10, 7))

# Esta es la funcion
plt.plot(x_vals, y_vals, label=f'f({v})', color='royalblue', linewidth=2)

# Puntos maximos en morado
if len(xmaximos) > 0:
    # Dibuja los puntos
    plt.scatter(xmaximos, ymaximos, color='purple', s=100, zorder=5, label='Máximos')
    
    # Coloca la coordenada a cada maximo
    for x_sym, y_sym in zip(xmaximos, ymaximos):
        # Convierte a decimal
        x_val = float(sympify(x_sym).evalf())
        y_val = float(sympify(y_sym).evalf())
        #Coloca maximo 2 decimales para no saturar la grafica
        texto = f"({x_val:.2f}, {y_val:.2f})"
        
        # Mueve las coordenadas un poco arriba para que sean visibles
        plt.annotate(texto, xy=(x_val, y_val), xytext=(0, 10), 
                     textcoords="offset points", ha='center', 
                     color='darkred', fontweight='bold')

# Puntos minimos en verde
if len(xminimos) > 0:
    # Dibuja los puntos
    plt.scatter(xminimos, yminimos, color='green', s=100, zorder=5, label='Mínimos')
    
    # Coloca coordenadas a cada mínimo
    for x_sym, y_sym in zip(xminimos, yminimos):
        # Lo mismo que en maximos
        x_val = float(sympify(x_sym).evalf())
        y_val = float(sympify(y_sym).evalf())
        texto = f"({x_val:.2f}, {y_val:.2f})"
        
        # Ahora mueve las coordenadas hacia abajo para que sean visibles
        plt.annotate(texto, xy=(x_val, y_val), xytext=(0, -20), 
                     textcoords="offset points", ha='center', 
                     color='darkgreen', fontweight='bold')

# Imprime la grafica ya generada con formato
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.grid(True, linestyle='--', alpha=0.7)
plt.title(f"Gráfica de {fin}")
plt.legend()
plt.tight_layout()

plt.show()
