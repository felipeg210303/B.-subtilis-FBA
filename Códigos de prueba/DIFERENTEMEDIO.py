import cobra
from cobra.io import read_sbml_model
import matplotlib.pyplot as plt

def configure_medium(model, medium_type="mínimo"):
    """
    Configura el medio de cultivo para el modelo iYO844.
    
    Parámetros:
    - model: Modelo metabólico cargado con COBRApy.
    - medium_type: "mínimo" para medio mínimo, "rico" para medio rico.
    """
    # Definir los medios como diccionarios {reacción: tasa}
    media = {
        "mínimo": {
            "EX_pi_LSQBKTe_RSQBKT": -3.0,  # Fosfato
            "EX_nh4_LSQBKTe_RSQBKT": -5.0, # Amonio
            "EX_so4_LSQBKTe_RSQBKT": -3.0, # Sulfato
            "EX_k_LSQBKTe_RSQBKT": -2.0,   # Potasio
            "EX_mg2_LSQBKTe_RSQBKT": -1.0, # Magnesio
            "EX_ca2_LSQBKTe_RSQBKT": -1.0, # Calcio
            "EX_na1_LSQBKTe_RSQBKT": -2.0, # Sodio
            "EX_o2_LSQBKTe_RSQBKT": -18.0  # Oxígeno
        },
        "rico": {
            "EX_h2o": -1000.0,    # Agua
            "EX_o2": -1000.0,     # Oxígeno
            "EX_co2": -1000.0,    # CO2
            "EX_ca2": -1000.0,    # Calcio
            "EX_h": -1000.0,      # H+
            "EX_k": -1000.0,      # Potasio
            "EX_mg2": -1000.0,    # Magnesio
            "EX_na1": -1000.0,    # Sodio
            "EX_fe3": -1000.0,    # Hierro Fe3+
            "EX_pi": -5.0,        # Fosfato
            "EX_glu__L": -1000.0, # Glutamato
            "EX_gly": -1000.0,    # Glicina
            "EX_zn2": -1000.0,    # Zinc
            "EX_ala__L": -5.0,    # Alanina
            "EX_lys__L": -5.0,    # Lisina
            "EX_asp__L": -5.0,    # Aspartato
            "EX_so4": -5.0,       # Sulfato
            "EX_arg__L": -5.0,    # Arginina
            "EX_ser__L": -5.0,    # Serina
            "EX_met__L": -5.0,    # Metionina
            "EX_trp__L": -5.0,    # Triptófano
            "EX_tyr__L": -5.0,    # Tirosina
            "EX_ura": -5.0,       # Uracilo
            "EX_leu__L": -5.0,    # Leucina
            "EX_his__L": -5.0,    # Histidina
            "EX_pro__L": -5.0,    # Prolina
            "EX_val__L": -5.0,    # Valina
            "EX_thr__L": -5.0,    # Treonina
            "EX_adn": -5.0,       # Adenosina
            "EX_thymd": -5.0,     # Timidina
            "EX_nico": -5.0,      # Nicotinato
            "EX_ribflv": -5.0,    # Riboflavina
            "EX_hxan": -5.0,      # Hipoxantina
            "EX_inost": -5.0,     # Inosina
            "EX_uri": -5.0,       # Uridina
            "EX_ile__L": -5.0,    # Isoleucina
            "EX_cys__L": -5.0,    # Cisteína
            "EX_fol": -5.0,       # Folato
            "EX_dad_2": -5.0,     # Desoxiadenosina
            "EX_hg2": -5.0,       # Mercurio Hg2+
            "EX_pnto__R": -5.0,   # Pantotenato
            "EX_dcyt": -5.0,      # Desoxicitidina
            "EX_cd2": -5.0,       # Cadmio
            "EX_crt": -5.0,       # Cromato
            "EX_phe__L": -5.0,    # Fenilalanina
            "EX_glc__D": -10.6    # D-Glucosa
        }
    }

    # Establecer el medio en el modelo
    model.medium = media[medium_type]
    print(f"Medio configurado como: {medium_type}")

# Cargar el modelo
model = read_sbml_model("C:/Users/felip/Desktop/python/TESIS/iYO844.xml")

# Simulación en ambos medios
crecimiento = {}

for medio in ["mínimo", "rico"]:
    configure_medium(model, medio)
    solution = model.optimize()
    crecimiento[medio] = solution.objective_value
    print(f"Tasa de crecimiento en {medio}: {solution.objective_value:.4f} 1/h")

# Graficar crecimiento
plt.figure(figsize=(6, 4))
plt.bar(crecimiento.keys(), crecimiento.values(), color=['blue', 'green'])
plt.xlabel("Tipo de Medio")
plt.ylabel("Tasa de Crecimiento (1/h)")
plt.title("Comparación del Crecimiento en Diferentes Medios")
plt.ylim(0, max(crecimiento.values()) * 1.2)
plt.show()
