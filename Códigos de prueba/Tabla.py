import cobra
from cobra.io import read_sbml_model
import matplotlib.pyplot as plt

def simulate_carbon_sources():
    # Cargar el modelo
    model = read_sbml_model("C:/Users/felip/Desktop/python/TESIS/iYO844.xml")

    # Diccionario con fuentes de carbono y sus tasas de consumo (en mmol/gDW/h)
    carbon_sources = {
        "Etanol": ("EX_etoh_LSQBKTe_RSQBKT", -8.71),
        "D-Fructosa": ("EX_fru_LSQBKTe_RSQBKT", -8.71),
        "Fumarato": ("EX_fum_LSQBKTe_RSQBKT", -8.71),
        "D-Glucosa": ("EX_glc__D_LSQBKTe_RSQBKT", -8.71),
        "L-Glutamina": ("EX_gln__L_LSQBKTe_RSQBKT", -8.71),
        "L-Glutamato": ("EX_glu__L_LSQBKTe_RSQBKT", -8.71),
        "L-Lactato": ("EX_lac__L_LSQBKTe_RSQBKT", -8.71),
        "L-Malato": ("EX_mal__D_LSQBKTe_RSQBKT", -8.71),
        "Piruvato": ("EX_pyr_LSQBKTe_RSQBKT", -8.71),
        "Succinato": ("EX_succ_LSQBKTe_RSQBKT", -8.71)
    }
    
    # Identificadores de los nutrientes esenciales en un medio mínimo
    essential_nutrients = {
    "Fosfato": ("EX_pi_LSQBKTe_RSQBKT", -3.0),
    "Amonio": ("EX_nh4_LSQBKTe_RSQBKT", -5.0),
    "Sulfato": ("EX_so4_LSQBKTe_RSQBKT", -3.0),
    "Potasio": ("EX_k_LSQBKTe_RSQBKT", -2.0),
    "Magnesio": ("EX_mg2_LSQBKTe_RSQBKT", -1.0),
    "Calcio": ("EX_ca2_LSQBKTe_RSQBKT", -1.0),
    "Sodio": ("EX_na1_LSQBKTe_RSQBKT", -2.0),
    "Oxígeno": ("EX_o2_LSQBKTe_RSQBKT", -18)
}
    
    # Diccionario para guardar la tasa de crecimiento obtenida con cada fuente de carbono
    growth_rates = {}

    # Iterar sobre cada fuente de carbono
    for carbon, (rxn_id, uptake_rate) in carbon_sources.items():
      
        # Resetear todas las fuentes de carbono a un valor muy bajo (bloquearlas)
        for reaction in model.exchanges:
            reaction.lower_bound = -1.5

        # Configurar el medio mínimo con los nutrientes esenciales
        for nutrient, (nutrient_rxn, value) in essential_nutrients.items():
            try:
                model.reactions.get_by_id(nutrient_rxn).lower_bound = value
            except KeyError:
                print(f"⚠️ Advertencia: No se encontró la reacción {nutrient_rxn} en el modelo.")

        # Establecer la fuente de carbono actual
        try:
            model.reactions.get_by_id(rxn_id).lower_bound = uptake_rate
        except KeyError:
            print(f"⚠️ Advertencia: No se encontró la reacción {rxn_id} para {carbon}.")
            continue
        
        # Optimizar el modelo
        solution = model.optimize()
        growth_rate = round(solution.objective_value, 4)  # Redondear a 4 decimales
        growth_rates[carbon] = growth_rate
        print(f"Fuente: {carbon}  -> Crecimiento simulado: {growth_rate} 1/h")
        print("Límite de glucosa:", model.reactions.get_by_id("EX_glc__D_LSQBKTe_RSQBKT").lower_bound)
        print("Límite de fum:", model.reactions.get_by_id("EX_fum_LSQBKTe_RSQBKT").lower_bound)

    # Graficar los resultados
    plt.figure(figsize=(10, 6))
    plt.bar(growth_rates.keys(), growth_rates.values(), color="skyblue")
    plt.xlabel("Fuente de Carbono")
    plt.ylabel("Velocidad de Crecimiento (1/h)")
    plt.title("Comparación de crecimiento en diferentes fuentes de carbono")
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

if __name__ == "__main__":
    simulate_carbon_sources()
