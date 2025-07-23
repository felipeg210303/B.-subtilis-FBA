# Importamos las librerías necesarias
import cobra
import matplotlib.pyplot as plt
import numpy as np
from cobra.io import load_model

# Cargamos el modelo de ejemplo proporcionado por COBRApy
model = load_model("textbook")

# Realizamos FBA (Análisis de Balance de Flujo)
solution = model.optimize()
print("\nSolución del FBA:")
print(solution)

# Seleccionamos dos reacciones clave para graficar el espacio de solución
reaction1 = model.reactions.get_by_id("PFK")  # Fosfofructoquinasa
reaction2 = model.reactions.get_by_id("PGI")  # Fosfoglucosa isomerasa

# Definimos un rango de valores para la reacción1
flux_range = np.linspace(reaction1.lower_bound, reaction1.upper_bound, 100)
fluxes_reaction2 = []

for flux in flux_range:
    with model:
        # Fijamos el flujo de la primera reacción
        reaction1.lower_bound = reaction1.upper_bound = flux
        # Resolvemos de nuevo para encontrar el flujo asociado a reaction2
        solution = model.optimize()
        fluxes_reaction2.append(solution.fluxes[reaction2.id])

# Graficamos el espacio de solución
plt.figure(figsize=(8, 6))
plt.plot(flux_range, fluxes_reaction2, label=f"{reaction2.name} vs {reaction1.name}")
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.title("Espacio de Solución FBA")
plt.xlabel(f"Flujo de {reaction1.name} ({reaction1.id})")
plt.ylabel(f"Flujo de {reaction2.name} ({reaction2.id})")
plt.legend()
plt.grid(True)
plt.show()
