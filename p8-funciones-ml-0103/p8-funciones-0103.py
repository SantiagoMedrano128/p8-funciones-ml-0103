#Santiago Medrano NC 0103
#NL 41 pythones

#Matematicas
print("+-+-+-+-MATEMATICAS-+-+-+-+-+")
def funcion_matematica(x):
    return x ** 2

# Entrada: x = -4
entrada_x = -4

# Salida: g(-4) = 16
salida_y = funcion_matematica(entrada_x)

print(f"Entrada: {entrada_x}")
print(f"Salida: {salida_y}")

#PROGRAMACION
print("+-+-+-+-PROGRAMACION-+-+-+-+-+")
def es_par(numero):
    return numero % 2 == 0

# Entrada: numero = 8
entrada_num = 8

# Salida: True
resultado = es_par(entrada_num)

print(f"Entrada: {entrada_num}")
print(f"Salida: {resultado}")

#CUERPO HUMANO
print("+-+-+-+-CUERPO HUMANO-+-+-+-+-+")
def funcion_rinon(sangre_con_desechos):
    # Proceso de filtrado
    sangre_filtrada = [item for item in sangre_con_desechos if not item.startswith("desecho")]
    orina = [item for item in sangre_con_desechos if item.startswith("desecho")]
    
    return sangre_filtrada, orina

# Entrada
sangre_entrada = ["glóbulos_rojos", "agua", "desecho_urea", "proteínas", "desecho_acido_urico"]

# Salida
sangre_limpia, desechos_excretados = funcion_rinon(sangre_entrada)

print(f"Entrada: {sangre_entrada}")
print(f"Salida - Sangre filtrada: {sangre_limpia}")
print(f"Salida - Orina: {desechos_excretados}")

#Vegetales (Fotosíntesis)
print("+-+-+-+-VEGETALES(FOTOSINTESIS)-+-+-+-+-+")
def respiracion_celular(glucosa_moles, oxigeno_moles):
    # Estequiometría: 1 C6H12O6 + 6 O2 -> 6 CO2 + 6 H2O + ATP
    if glucosa_moles >= 1 and oxigeno_moles >= 6:
        co2_moles = 6
        agua_moles = 6
        atp_energia = "36-38 ATP"
        return co2_moles, agua_moles, atp_energia
    else:
        return 0, 0, "0 ATP (Insumos insuficientes)"

# Entrada
entradas = {"glucosa": 1, "oxigeno": 6}

# Salida
co2, agua, energia = respiracion_celular(entradas["glucosa"], entradas["oxigeno"])

print(f"Entradas: {entradas}")
print(f"Salidas: {co2} moles CO2, {agua} moles H2O, Energía: {energia}")

#INGENIERIA
print("+-+-+-+-INGENIERIA-+-+-+-+-+")
def freno_de_disco(presion_pedal_psi, velocidad_actual_kmh):
    # Convierte energía cinética en calor mediante fricción
    reduccion_velocidad = presion_pedal_psi * 0.5
    nueva_velocidad = max(0, velocidad_actual_kmh - reduccion_velocidad)
    calor_generado_joules = presion_pedal_psi * 120  # Estimación
    
    return nueva_velocidad, calor_generado_joules

# Entrada
presion = 40  # psi
velocidad_inicial = 80  # km/h

# Salida
velocidad_final, calor = freno_de_disco(presion, velocidad_inicial)

print(f"Entradas: Presión = {presion} psi, Velocidad = {velocidad_inicial} km/h")
print(f"Salida: Nueva Velocidad = {velocidad_final} km/h, Calor disipado = {calor} Joules")

print("Santiago Medrano Segundo NC 0103  NL 41")
