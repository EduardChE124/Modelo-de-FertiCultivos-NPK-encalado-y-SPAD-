
# ==============================================================================
# MODELO RACIONAL DE FERTILIZACIÓN NPK AVANZADO 
# Incorpora: MOS, Rastrojos, N en Agua de Riego y Diagnóstico/Corrección de pH
# ==============================================================================

# TABLA COMPLETA DE PARÁMETROS POR CULTIVO Y HORTALIZAS 

CULTIVOS = {
    # --- CULTIVOS TRADICIONALES ---
    "Trigo":             {"HC": 0.15, "IC": 0.42, "RI_N": 1.2, "RI_P": 0.20, "RI_K": 0.8, "CAR": 1.7, "pH_critico": 6.0, "SPAD_ref": 45.0},
    "Maravilla":         {"HC": 0.14, "IC": 0.36, "RI_N": 1.2, "RI_P": 0.20, "RI_K": 1.0, "CAR": 1.5, "pH_critico": 6.0, "SPAD_ref": 42.0},
    "Cebada":            {"HC": 0.15, "IC": 0.48, "RI_N": 1.2, "RI_P": 0.20, "RI_K": 0.8, "CAR": 1.7, "pH_critico": 6.0, "SPAD_ref": 44.0},
    "Frejoles":          {"HC": 0.14, "IC": 0.40, "RI_N": 2.3, "RI_P": 0.28, "RI_K": 1.8, "CAR": 1.5, "pH_critico": 6.0, "SPAD_ref": 42.0},
    "Garbanzos":         {"HC": 0.12, "IC": 0.45, "RI_N": 2.8, "RI_P": 0.30, "RI_K": 1.8, "CAR": 1.5, "pH_critico": 6.0, "SPAD_ref": 40.0},
    "Arvejas":           {"HC": 0.10, "IC": 0.36, "RI_N": 2.6, "RI_P": 0.28, "RI_K": 1.5, "CAR": 1.5, "pH_critico": 6.0, "SPAD_ref": 40.0},
    "Lentejas":          {"HC": 0.14, "IC": 0.32, "RI_N": 2.4, "RI_P": 0.25, "RI_K": 1.2, "CAR": 1.5, "pH_critico": 6.0, "SPAD_ref": 38.0},
    "Arroz":             {"HC": 0.15, "IC": 0.45, "RI_N": 1.0, "RI_P": 0.16, "RI_K": 0.8, "CAR": 1.7, "pH_critico": 5.5, "SPAD_ref": 40.0},
    "Maiz":              {"HC": 0.15, "IC": 0.48, "RI_N": 1.0, "RI_P": 0.16, "RI_K": 0.7, "CAR": 1.7, "pH_critico": 6.0, "SPAD_ref": 50.0},
    "Raps":              {"HC": 0.10, "IC": 0.21, "RI_N": 1.2, "RI_P": 0.20, "RI_K": 1.0, "CAR": 1.5, "pH_critico": 6.0, "SPAD_ref": 45.0},
    "Remolacha":         {"HC": 0.80, "IC": 0.65, "RI_N": 1.0, "RI_P": 0.16, "RI_K": 2.0, "CAR": 1.5, "pH_critico": 6.1, "SPAD_ref": 48.0},
    "Papas":             {"HC": 0.80, "IC": 0.75, "RI_N": 1.1, "RI_P": 0.18, "RI_K": 2.5, "CAR": 1.0, "pH_critico": 5.5, "SPAD_ref": 45.0},
    "Ballica Italiana":  {"HC": 0.75, "IC": 0.90, "RI_N": 1.6, "RI_P": 0.20, "RI_K": 0.8, "CAR": 1.7, "pH_critico": 5.8, "SPAD_ref": 38.0},
    "Avena":             {"HC": 0.15, "IC": 0.40, "RI_N": 1.2, "RI_P": 0.20, "RI_K": 0.8, "CAR": 1.7, "pH_critico": 5.4, "SPAD_ref": 42.0},

    # --- HORTALIZAS Y OTROS ---
    "Acelga":            {"HC": 0.93, "IC": 0.90, "RI_N": 2.5, "RI_P": 0.50, "RI_K": 3.7, "CAR": 1.0, "pH_critico": 6.2, "SPAD_ref": 48.0},
    "Cebolla":           {"HC": 0.90, "IC": 0.85, "RI_N": 1.2, "RI_P": 0.20, "RI_K": 1.6, "CAR": 1.0, "pH_critico": 6.0, "SPAD_ref": 52.0},
    "Lechuga":           {"HC": 0.95, "IC": 0.90, "RI_N": 2.5, "RI_P": 0.40, "RI_K": 3.5, "CAR": 1.0, "pH_critico": 6.0, "SPAD_ref": 35.0},
    "Melon":             {"HC": 0.88, "IC": 0.75, "RI_N": 1.8, "RI_P": 0.40, "RI_K": 2.4, "CAR": 1.0, "pH_critico": 6.0, "SPAD_ref": 45.0},
    "Tomate":            {"HC": 0.94, "IC": 0.64, "RI_N": 2.2, "RI_P": 0.30, "RI_K": 4.5, "CAR": 1.0, "pH_critico": 6.0, "SPAD_ref": 52.0},
    "Zapallo":           {"HC": 0.91, "IC": 0.36, "RI_N": 1.8, "RI_P": 0.20, "RI_K": 4.1, "CAR": 1.0, "pH_critico": 6.0, "SPAD_ref": 48.0},
    "Lúpulo":            {"HC": 0.75, "IC": 0.90, "RI_N": 1.8, "RI_P": 0.30, "RI_K": 2.0, "CAR": 1.0, "pH_critico": 6.0, "SPAD_ref": 45.0},
    "Zanahoria":          {"HC": 0.90, "IC": 0.80, "RI_N": 1.5, "RI_P": 0.25, "RI_K": 2.0, "CAR": 1.0, "pH_critico": 5.5, "SPAD_ref": 45.0},
    "Brocoli":            {"HC": 0.90, "IC": 0.85, "RI_N": 2.0, "RI_P": 0.35, "RI_K": 2.5, "CAR": 1.0, "pH_critico": 6.2, "SPAD_ref": 58.0},
    "Coliflor":           {"HC": 0.92, "IC": 0.85, "RI_N": 2.0, "RI_P": 0.35, "RI_K": 2.5, "CAR": 1.0, "pH_critico": 6.2, "SPAD_ref": 55.0},
    "Pepino":             {"HC": 0.95, "IC": 0.75, "RI_N": 1.8, "RI_P": 0.35, "RI_K": 2.5, "CAR": 1.0, "pH_critico": 6.0, "SPAD_ref": 46.0},
    "Pimiento":           {"HC": 0.93, "IC": 0.65, "RI_N": 2.0, "RI_P": 0.35, "RI_K": 3.0, "CAR": 1.0, "pH_critico": 6.0, "SPAD_ref": 52.0},
    "Berenjena":          {"HC": 0.93, "IC": 0.65, "RI_N": 2.0, "RI_P": 0.35, "RI_K": 3.0, "CAR": 1.0, "pH_critico": 6.0, "SPAD_ref": 50.0},
    "Sandia":             {"HC": 0.92, "IC": 0.70, "RI_N": 1.8, "RI_P": 0.35, "RI_K": 2.5, "CAR": 1.0, "pH_critico": 5.5, "SPAD_ref": 48.0},
}
 
# Referencias: 
    #- Havlin, J. L., Tisdale, S. L., Nelson, W. L., & Beaton, J. D. (2014). Soil fertility and fertilizers: An introduction
    # to nutrient management (8th ed.). Pearson.

    #- Marschner, P. (Ed.). (2012). Marschner's mineral nutrition of higher plants (3rd ed.). Academic Press. 
    # https://doi.org/10.1016/C2009-0-63043-9

    #- Food and Agriculture Organization of the United Nations. (2006). Plant nutrition for food security: A guide for
    # integrated nutrient management (FAO Fertilizer 
    # and Plant Nutrition Bulletin No. 16). FAO. https://www.fao.org/4/a0443e/a0443e00.htm
def calcular_dosis_npk_avanzado(
    cultivo=None,
    rendimiento_kgha=None,
    ppm_n_suelo=None,
    ppm_p_suelo=None,
    ppm_k_suelo=None,
    da=None,
    profundidad_cm=None,
    ct_p=None,
    car_p=None,
    eficiencia_n=None,
    eficiencia_k=None,
    

    mos_pct=0,                      # Materia Orgánica del Suelo (%)
    tasa_mineralizacion_mos=0.2,     # Mineralización anual de la MOS (2% = 0.02)
    
    incorporar_rastrojo=False,        # ¿Se incorpora rastrojo del cultivo anterior? (True/False)
    rastrojo_ton_ha=None,             # Toneladas rastrojo/ha (si es None, lo calcula automáticamente)
    kg_n_por_ton_rastrojo=8.0,        # kg de N por ton de rastrojo (ej. Maíz ~8 kg/ton)
    pct_min_rastrojo=0.40,            # Mineralización del rastrojo (40% = 0.40)
    
    ppm_n_agua=0.0,                   # Concentración de N en agua de riego (ppm o mg/L)
    volumen_riego_m3ha=0.0,           # Volumen de agua de riego aplicado (m3/ha)
    
    ph_suelo=6.4,                     # pH del suelo
    ct_ph=0.12,                        # Capacidad Tampón pH (0.12 Trumao, 0.15 Rojo Arcilloso, 0.20 Aluvial)
    spad_sector=42.5, # Lectura promedio del potrero 
    
):
    p = CULTIVOS[cultivo]
    if car_p is None:
        car_p = p["CAR"]
        
    # Masa de suelo por hectárea (kg/ha)
    profundidad_m = profundidad_cm / 100.0
    masa_suelo_kgha = 10000.0 * profundidad_m * (da * 1000.0)
    
    # --------------------------------------------------------------------------
    # APORTES Y BALANCE DE NITRÓGENO
    # --------------------------------------------------------------------------
    # a) N inorgánico del suelo (NO3 + NH4)
    suministro_n_suelo = ppm_n_suelo * da * (profundidad_cm / 10.0)
    
    # b) Mineralización de la Materia Orgánica del Suelo (MOS)
    n_organico_mos_kgha = masa_suelo_kgha * (mos_pct / 100.0) * 0.05
    n_min_mos_kgha = n_organico_mos_kgha * tasa_mineralizacion_mos
    
    # c) Aporte por incorporación de rastrojo
    n_min_rastrojo_kgha = 0.0
    if incorporar_rastrojo:
        if rastrojo_ton_ha is None:
            # Estimación a partir del rendimiento y del Índice de Cosecha (IC)
            ms_total_kgha = (rendimiento_kgha * (1.0 - p["HC"])) / p["IC"]
            grano_ms_kgha = rendimiento_kgha * (1.0 - p["HC"])
            rastrojo_ton_ha = max(0.0, (ms_total_kgha - grano_ms_kgha) / 1000.0)
        
        n_tot_rastrojo = rastrojo_ton_ha * kg_n_por_ton_rastrojo
        n_min_rastrojo_kgha = n_tot_rastrojo * pct_min_rastrojo
        
    # d) Aporte de N en el agua de riego
    n_agua_kgha = (ppm_n_agua * volumen_riego_m3ha) / 1000.0
    
    # SUMINISTRO TOTAL DE NITRÓGENO
    suministro_n_total = suministro_n_suelo + n_min_mos_kgha + n_min_rastrojo_kgha + n_agua_kgha
    
    # Demanda y Dosis de N
    demanda_n = (rendimiento_kgha * (1.0 - p["HC"]) * (p["RI_N"] / 100.0)) / p["IC"]
    dosis_n_base = max(0.0, (demanda_n - suministro_n_total) / eficiencia_n)
    
    # --------------------------------------------------------------------------
  #DIAGNÓSTICO FOLIAR SPAD / NDVI 
    # -------------------------------------------------------------------------- 
    pct_suficiencia_spad = (spad_sector / p["SPAD_ref"]) * 100.0 
    
    if pct_suficiencia_spad < 95.0: 
        # Incrementa la dosis proporcionalmente al déficit observado 
        factor_spad = 1.0 + ((95.0 - pct_suficiencia_spad) / 100.0) 
    elif pct_suficiencia_spad > 105.0: 
            factor_spad = 0.90 
    else: factor_spad = 1.0       
    # Dosis de Nitrógeno ajustada en tiempo real por clorofila foliar 
    dosis_n_final = dosis_n_base * factor_spad
    
    # --------------------------------------------------------------------------
    # FÓSFORO (P2O5)
    # --------------------------------------------------------------------------
    demanda_p_kg = (rendimiento_kgha * (1.0 - p["HC"]) * (p["RI_P"] / 100.0)) / p["IC"]
    ppm_p_deseado = demanda_p_kg / car_p
    dosis_p2o5 = max(0.0, (ppm_p_deseado - ppm_p_suelo) * ct_p * 2.3)
    
    # --------------------------------------------------------------------------
    # POTASIO (K2O)
    # --------------------------------------------------------------------------
    demanda_k_kg = (rendimiento_kgha * (1.0 - p["HC"]) * (p["RI_K"] / 100.0)) / p["IC"]
    suministro_k = ppm_k_suelo * da * (profundidad_cm / 10.0)
    dosis_k2o = max(0.0, ((demanda_k_kg - suministro_k) / eficiencia_k) * 1.2)
    
    # --------------------------------------------------------------------------
    # 4. EVALUACIÓN DE pH Y REQUERIMIENTO DE ENMIENDAS
    # --------------------------------------------------------------------------
    ph_critico = p.get("pH_critico", 6.0)
    dosis_cal_ton_ha = 0.0
    diagnostico_ph = ""
    
    if ph_suelo < ph_critico:
        dosis_cal_ton_ha = (ph_critico - ph_suelo) / ct_ph
        diagnostico_ph = f"Suelo Ácido (pH {ph_suelo} < crítico {ph_critico}). Requiere encalado."
    elif ph_suelo > 7.8:
        diagnostico_ph = f"Suelo Alcalino (pH {ph_suelo}). Riesgo de fijación de P"
    else:
        diagnostico_ph = f"pH Óptimo ({ph_suelo}). En rango adecuado para {cultivo}."

 
    return {
        "Cultivo": cultivo,
        "Rendimiento (t/ha)": rendimiento_kgha / 1000.0,
        "Demanda N Total (kg/ha)": round(demanda_n, 1),
        "Demanda P Total (kg/ha)": round(demanda_p_kg, 1),
        "Demanda K Total (kg/ha)": round(demanda_k_kg, 1),
        "--- APORTES ---": "",
        "  Suministro N Inorgánico Suelo (kg/ha)": round(suministro_n_suelo, 1),
        "  Mineralización de MOS (kg/ha)": round(n_min_mos_kgha, 1),
        "  Aporte Rastrojo Incorporado (kg/ha)": round(n_min_rastrojo_kgha, 1),
        "  Aporte N Agua de Riego (kg/ha)": round(n_agua_kgha, 1),
        "Suministro N Total (kg/ha)": round(suministro_n_total, 1),
        "Dosis Base N (kg N/ha)": round(dosis_n_base, 1),
        "--- DIAGNÓSTICO FOLIAR SPAD / NDVI ---": "",
        "Diagnóstico SPAD": {
            "SPAD Sector / Referencia": f"{spad_sector} / {p["SPAD_ref"]}",
            "Porcentaje Suficiencia": f"{pct_suficiencia_spad:.1f}%",
            "Factor Corrección N": f"x{factor_spad:.2f}"
        },
        "Dosis Nitrógeno Ajustada SPAD (kg N/ha)": round(dosis_n_final, 1),
        "Dosis Fósforo (kg P2O5/ha)": round(dosis_p2o5, 1),
        "Dosis Potasio (kg K2O/ha)": round(dosis_k2o, 1),
        "--- DIAGNÓSTICO DE pH Y ENMIENDAS ---": "",
        "Diagnóstico pH": diagnostico_ph,
        "Dosis Cal Agrícola (ton CaCO3/ha)": round(dosis_cal_ton_ha, 2)
    }

# ==============================================================================
# DATOS DE ENTRADA
# ==============================================================================

cultivo = "Trigo"
rendimiento_kgha = 12000

ppm_n_suelo = 9
ppm_p_suelo = 10
ppm_k_suelo = 186

da = 0.9
profundidad_cm = 20

ct_p = 12.0
eficiencia_n = 0.65  # Textura gruesa con riego excesivo: 40%; Textura media-fina con riego excesivo: 57%; Cualquier textura con riego óptimo: 50-65%; Fertilizantes de entrega lenta / Fertirriego eficiente: > 65%     
eficiencia_k = 0.75  # Arcilloso(2:1)-0.45; Arcilloso(1:1)-0.60; Franco-0.75; Arenoso-0.80


# ==============================================================================
# CÁLCULO DE LAS DOSIS NPK
# ==============================================================================

resultado = calcular_dosis_npk_avanzado(
    cultivo=cultivo,
    rendimiento_kgha=rendimiento_kgha,
    ppm_n_suelo=ppm_n_suelo,
    ppm_p_suelo=ppm_p_suelo,
    ppm_k_suelo=ppm_k_suelo,
    da=da,
    profundidad_cm=profundidad_cm,
    ct_p=ct_p,
    eficiencia_n=eficiencia_n,
    eficiencia_k=eficiencia_k
)

for clave, valor in resultado.items():
    if clave.startswith("---"):
        print("\n" + clave.replace("-", "").strip())
        print("-" * 100)
    elif isinstance(valor, float):
        print(f"{clave}: {valor:.2f}")
    else:
        print(f"{clave}: {valor}")





