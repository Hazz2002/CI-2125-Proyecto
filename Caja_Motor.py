import pandas as pd

# Cargar los datos desde el archivo de Excel
data = pd.read_csv("Datos_Ascensores.xls")

def Calculos(fila):
    grupo = data[fila, 0]
    Carga_Nominal = data[fila, 9]

    # Definir M_Cabina según la fila
    if fila <= 3:
        M_Cabina == 600
    else:
        M_Cabina = 700
    
    M_Contrapeso = (Carga_Nominal / 2) + M_Cabina
    Gravedad = "9.8"

    Vtan_Polea = data[fila, 6]
    Radio_Polea = 0.2
    Vang_Polea = Vtan_Polea * Radio_Polea
    Tension = M_Cabina * Gravedad
    Torque_Polea = Tension + Radio_Polea
    Potencia_Polea = Torque_Polea * Vtan_Polea
    Potencia_Caja = Potencia_Polea * 0.8
    Potencia_Motor = Potencia_Caja * 0.9
    Nro_Engranes = 376.99 / Potencia_Caja

    # Imprimir resultados en la terminal
    print(f"\n--- Resultados para {grupo} ---\n")
    print(f"Contrapeso: {M_Contrapeso} kg")
    print(f"Cabina: {M_Cabina} kg")
    print(f"Tensión: {Tension} N\n")
    print(f"Radio de la polea: {Radio_Polea} m")
    print(f"Torque de la polea: {Torque_Polea} Nm\n")
    print(f"Potencia de la polea: {Potencia_Polea} W")
    print(f"Potencia de la caja: {Potencia_Caja} W")
    print(f"Potencia del motor: {Potencia_Motor} W\n")
    print(f"Velocidad angular de la polea: {Vang_Polea} rad/s")
    print(f"Número de engranajes: {int(Nro_Engranes)} engranajes\n")
    print("=" * 50)

# Ejecutar cálculos para las diferentes filas
for i in range(1, 5):
    Calculos(i)
