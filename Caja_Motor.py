"""
Considerando una caja de cambio mecánica con un 80% de eficiencia que reduce
la velocidad del motor a la de la polea del ascensor.

Calculando el motor eléctrico con un 90% de eficiencia que gira a 3600 RPM.
"""
import pandas as pd

# Cargar los datos desde el archivo de Excel
de = pd.read_excel("Datos_Ascensores.xls")

def Calculos(fila):
    grupo = de.iloc[fila, 0]
    Carga_Nominal = de.iloc[fila, 9]  # kg
     # Definir M_Cabina según la fila
    if fila < 4:
        M_Cabina = 600  # kg para los tres primeros casos
    else:
        M_Cabina = 700  # kg para el último caso

    M_Contrapeso = (Carga_Nominal / 2) + M_Cabina  # kg
    Gravedad = 9.8

    Vtan_Polea = de.iloc[fila, 6]  # m/s
    Radio_Polea = 0.2
    Vang_Polea = Vtan_Polea / Radio_Polea
    Tension = M_Cabina * Gravedad  # N
    Torque_Polea = Tension * Radio_Polea
    Potencia_Polea = Torque_Polea * Vang_Polea
    Potencia_Caja = 10 * Potencia_Polea / 8
    Potencia_Motor = 10 * Potencia_Caja / 9
    Nro_Engranes = 376.99 / Vang_Polea

    # Imprimir resultados en la terminal
    print(f"\n--- Resultados para {grupo} ---\n")
    print(f"Contrapeso: {M_Contrapeso:.2f} kg")
    print(f"Cabina: {M_Cabina:.2f} kg")
    print(f"Tensión: {Tension:.2f} N\n")
    print(f"Radio de la polea: {Radio_Polea:.2f} m")
    print(f"Torque de la polea: {Torque_Polea:.2f} Nm\n")
    print(f"Potencia de la polea: {Potencia_Polea:.2f} W")
    print(f"Potencia de la caja: {Potencia_Caja:.2f} W")
    print(f"Potencia del motor: {Potencia_Motor:.2f} W\n")
    print(f"Velocidad angular de la polea: {Vang_Polea:.2f} rad/s")
    print(f"Número de engranajes: {round(Nro_Engranes)} engranajes\n")
    print("=" * 50)

# Ejecutar cálculos para las diferentes filas
for i in range(1, 5):  # Asumiendo que hay 4 grupos
    Calculos(i)