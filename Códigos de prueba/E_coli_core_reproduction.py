import cobra
import matplotlib.pyplot as plt
import numpy as np
import os

# Cargar un modelo metabólico 
model = cobra.io.read_sbml_model ('C:/Users/felip/Desktop/python/TESIS/Ec_core_flux1.xml')

# for rxn in model.exchanges:
#     rxn.lower_bound = 0 


model.reactions.get_by_id("EX_o2_e_").lower_bound = -1000 # Consumo de O2
model.reactions.get_by_id("EX_glc_e_").lower_bound = -1  #

# Optimizar el modelo con FBA
solution = model.optimize()
print(f'Objective value: {solution.objective_value}')

# Obtener los flujos de las reacciones
fluxes = solution.fluxes

# # Graficar
# reactions = list(fluxes.index)
# values = list(fluxes.values)

# plt.figure(figsize=(10, 6))
# plt.barh(reactions, values, color='skyblue')
# plt.axvline(0, color='grey', lw=0.8)  # Línea vertical en x=0
# plt.title('Flujos de Reacción del Modelo Metabólico')
# plt.xlabel('Flujo')
# plt.ylabel('Reacciones')
# plt.grid(axis='x')
# plt.show()
