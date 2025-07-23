# NO FUNCIONA, EL MODELO 1147 PARECE SER INVÁLIDO, TENGO QUE BUSCAR O PREGUNTAR A LOS AUTORES POR QUÉ PASA ESO


import cobra
import matplotlib.pyplot as plt
import numpy as np

# Cargar un modelo metabólico
model = cobra.io.read_sbml_model("C:/Users/felip/Desktop/python/TESIS/iBsu1147_1.xml")

for reaction in model.reactions:
    reaction.lower_bound = -1  # Reacción inicial con límite inferior a 0

for reaction in model.exchanges:
    reaction.lower_bound = -10 

# Optimizar el modelo con FBA
solution=model.optimize()


print(f'Valor objetivo: {solution.objective_value}')

# Obtener los flujos de las reacciones para graficar
fluxes = solution.fluxes

# Graficar
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