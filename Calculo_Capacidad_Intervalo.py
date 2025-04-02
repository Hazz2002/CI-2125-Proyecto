import numpy
import pandas as pd

# Cargar los datos desde el archivo de Excel
de = pd.read_excel("Datos_Ascensores.xls")

def main(fila):
    Res_Grupo = de.iloc[fila, 0]
    print(f"\n{Res_Grupo}\n")

    # Datos proporcionados
    Poblacion_Piso = 20
    Poblacion_Sotano = 16
    Sotanos_servidos=2

    # Parámetros de pisos y tiempos
    Distancia_Promedio = 3.5  # m (EP)
    Distancia_Promedio_Par = 7  # (PV)
    Recorrido_Ppal_Super = 7.37  # (HP)
    Recorrido_Total = 10  # (TP)
    Distancia_Expresa_A1 = 7.00  # (EA1)
    Distancia_Expresa_A2 = 7.00  # (EA2)
    Distancia_Expresa_A3 = 7  # (EA3)
    Tiempo_Viaje_C1 = 130.73  # (TVC1)
    Tiempo_Viaje_C2 = 130.73  # (TVC2)
    Tiempo_Viaje_C3 = 130.73  # (TVC3)
    Tiempo_Apertura_Cierre = 4.58  # (TA1, TA2, TA3)
    Tiempo_Total_Viaje = 135.30  # (TTV)
    Capacidad_Transporte = 8.0837  # (C)



    # Datos del archivo
    Pisos_Servidos = round(float(de.iloc[fila, 2]))  # Redondeado a entero
    Pisos_No_Servidos = round(float(de.iloc[fila, 3]))  # Redondeado a entero desde el Excel
    Pisos_Totales = Pisos_Servidos + Pisos_No_Servidos  # Total de pisos

    Nro_Ascensores = float(de.iloc[fila, 4])
    Capacidad_Nominal_P = float(de.iloc[fila, 5])
    Velocidad_Nominal_Establecida = float(de.iloc[fila, 6])  # m/s
    Tiempo_Entrada_Salida = float(de.iloc[fila, 8])  # s

    # Calculo de distancia Promedio entre pisos

    if fila < 4:
        DistanciaP_Pisos = 22*3.5/(Pisos_Servidos+3)
    else:
        DistanciaP_Pisos = 22*3.5/(Pisos_Servidos+2)


    # Determinar si hay zona expresa
    Zona_expresa = de.iloc[fila, 1] == "si"

    # Cálculo de la población total
    Poblacion_Total = (Poblacion_Piso * Pisos_Servidos) + (Poblacion_Sotano * Sotanos_servidos)

    # Personas por viaje
    Personas_Viaje = numpy.nan_to_num(int((3.2 / Capacidad_Nominal_P) + (0.7 * Capacidad_Nominal_P) + 0.5))

    # Número de paradas probables
    Paradas_Probables = Pisos_Servidos * (1 - (((Pisos_Servidos - 1) / Pisos_Servidos) ** Personas_Viaje))

    # Ajustar velocidad referencial
    Aceleracion = 1  # m/s²
    ReferenciaV_Nom = numpy.sqrt((Recorrido_Ppal_Super * Aceleracion) / Paradas_Probables)

    # Cálculo del tiempo de viaje
    if ReferenciaV_Nom < Velocidad_Nominal_Establecida and not Zona_expresa:
        Tiempo_Viaje_Completo = (
            (2 * Recorrido_Ppal_Super / numpy.sqrt(Recorrido_Ppal_Super * Aceleracion / Paradas_Probables)) +
            (Velocidad_Nominal_Establecida / Aceleracion) +
            (Recorrido_Ppal_Super / Velocidad_Nominal_Establecida) +
            (Tiempo_Apertura_Cierre * (Paradas_Probables + 1)) +
            (Tiempo_Entrada_Salida * Personas_Viaje)
        )

    elif ReferenciaV_Nom >= Velocidad_Nominal_Establecida and not Zona_expresa:
        Tiempo_Viaje_Completo = (
            (2 * Recorrido_Ppal_Super / Velocidad_Nominal_Establecida) +
            ((Velocidad_Nominal_Establecida / Aceleracion) + Tiempo_Apertura_Cierre) * (Paradas_Probables + 1) +
            (Tiempo_Entrada_Salida * Personas_Viaje)
        )

    elif ReferenciaV_Nom >= Velocidad_Nominal_Establecida and Zona_expresa:
        Tiempo_Viaje_Completo = (
            (2 * Recorrido_Ppal_Super / Velocidad_Nominal_Establecida) +
            ((Velocidad_Nominal_Establecida / Aceleracion) + Tiempo_Apertura_Cierre) * (Paradas_Probables + 1) -
            (Recorrido_Ppal_Super / (Paradas_Probables * Velocidad_Nominal_Establecida)) +
            (Tiempo_Entrada_Salida * Personas_Viaje)
        )

    else:
        Tiempo_Viaje_Completo = Tiempo_Total_Viaje  # Usar el valor proporcionado

    Tiempo_Adicional = (Tiempo_Viaje_Completo*3.5*2)/100

    Tiempo_Total_Viaje = Tiempo_Viaje_Completo + Tiempo_Adicional

    # Cálculo de la capacidad de transporte
    Capacidad_Transporte = (300 * DistanciaP_Pisos * Nro_Ascensores * 100) / (Tiempo_Total_Viaje * Poblacion_Total)
    Intervalo_Probable = Tiempo_Total_Viaje / Nro_Ascensores
    Tiempo_Llenado = 500 / Capacidad_Transporte

    # Imprimir resultados en la terminal
    print(f"Número de Ascensores: {Nro_Ascensores}")
    print(f"\nVel. Nominal establecida: {Velocidad_Nominal_Establecida} [m/s]")
    print(f"Velocidad Referencial: {ReferenciaV_Nom}")
    print(f"\nRecorrido Principal Superior: {Recorrido_Ppal_Super} m")
    print(f"Pisos servidos: {Pisos_Servidos}, Pisos NO servidos: {Pisos_No_Servidos}, Pisos totales: {Pisos_Totales}")
    print(f"Población total: {Poblacion_Total}")
    print(f"Paradas probables: {Paradas_Probables:.2f}")
    print(f"Personas por viaje: {Personas_Viaje}\n")
    print(f"Tiempo de apertura y cierre: {Tiempo_Apertura_Cierre} s")
    print(f"Tiempo de entrada y salida: {Tiempo_Entrada_Salida} s")
    print(f"Tiempo de Viaje Completo: {Tiempo_Viaje_Completo:.2f} s")
    print(f"Tiempo Total de Viaje: {Tiempo_Total_Viaje:.2f} s")
    print(f"\nCapacidad de Transporte [C]: {Capacidad_Transporte:.2f} %")
    print(f"Intervalo Probable [I]: {Intervalo_Probable:.2f} s")
    print(f"Tiempo de llenado: {Tiempo_Llenado:.2f} s\n")
    print (f"Distancia promedio entre pisos: {DistanciaP_Pisos:.2f}")
    return Res_Grupo, Zona_expresa, Pisos_Servidos, Pisos_No_Servidos, Pisos_Totales, Nro_Ascensores, \
           Velocidad_Nominal_Establecida, ReferenciaV_Nom, Recorrido_Ppal_Super, Tiempo_Apertura_Cierre, \
           Tiempo_Entrada_Salida, Tiempo_Viaje_Completo, Tiempo_Total_Viaje, Capacidad_Nominal_P, \
           Personas_Viaje, Poblacion_Total, Paradas_Probables, Capacidad_Transporte, Intervalo_Probable, Tiempo_Llenado


def run():
    for i in range(1, 5):  # Procesar 4 grupos
        main(i)
        print("\n--- Fin de cálculo para el grupo ---\n")


run()
