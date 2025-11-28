#Johan (Calculo de maximos y minimos)

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