# FUNCIONA, MUESTRA FLUJOS Y EL VALOR DE LA FUNCIÓN OBJETIVO, PERO ESTE ES MUY ALTO
# POR ESTO TENGO QUE VER SI ES UN ERROR DEL MODELO, SI ES COHERENTE CON LAS UNIDADES O SIMPLEMENTE ESTÁ MAL

import cobra
from cobra.io.sbml import validate_sbml_model
import matplotlib.pyplot as plt
import numpy as np

# Validar el modelo antes de cargarlo
model, errors = validate_sbml_model("C:/Users/felip/Desktop/python/TESIS/iBsu1103.xml")

# Verificar si hay errores en la validación
if errors:
    print("Errores en el modelo SBML:", errors)
else:
    print("El modelo SBML es válido.")

# Cargar el modelo metabólico
model = cobra.io.read_sbml_model("C:/Users/felip/Desktop/python/TESIS/iBsu1103.xml")

# Optimizar el modelo con FBA
solution = model.optimize()

# Mostrar el valor objetivo
print(f'Valor objetivo: {solution.objective_value}')

# Obtener los flujos de las reacciones
fluxes = solution.fluxes

# Graficar los flujos de reacción
reactions = list(fluxes.index)
values = list(fluxes.values)

plt.figure(figsize=(10, 6))
plt.barh(reactions, values, color="skyblue")

plt.axvline(0, color="grey", lw=0.8)  # Línea vertical en x=0
plt.title("Flujos de Reacción del Modelo Metabólico")
plt.xlabel("Flujo")
plt.ylabel("Reacciones")

plt.grid(axis='x')
plt.show()
