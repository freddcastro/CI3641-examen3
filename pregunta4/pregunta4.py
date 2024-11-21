import matplotlib.pyplot as plt

# Definir los tamaños de las matrices
tamanos_matriz = [
    "100x100", "100x1000", "100x10000", "100x100000", "100x1000000",
    "1000x100", "1000x1000", "1000x10000", "1000x100000", "1000x1000000",
    "10000x100", "10000x1000", "10000x10000", "10000x100000", "10000x1000000",
    "100000x100", "100000x1000", "100000x10000", "100000x100000"
]

# Tiempos de ejecución por fila para cada iteración
tiempos_fila_iter1 = [
    0.000011, 0.000095, 0.001467, 0.015469, 0.154082,
    0.000101, 0.000957, 0.014737, 0.157153, 1.541646,
    0.001181, 0.010014, 0.148634, 1.547460, 15.555999,
    0.010621, 0.096104, 1.483586, 15.297193
]
tiempos_fila_iter2 = [
    0.000013, 0.000095, 0.000955, 0.009522, 0.095500,
    0.000100, 0.000957, 0.009505, 0.095039, 0.948213,
    0.001172, 0.009933, 0.095786, 0.953886, 9.530409,
    0.010084, 0.097091, 0.956120, 9.489693
]
tiempos_fila_iter3 = [
    0.000010, 0.000095, 0.000969, 0.009500, 0.094758,
    0.000100, 0.000983, 0.013771, 0.095070, 0.952909,
    0.001102, 0.009669, 0.095263, 0.951021, 9.501469,
    0.010169, 0.097917, 0.948391, 9.497533
]

# Tiempos de ejecución por columna para cada iteración
tiempos_columna_iter1 = [
    0.000011, 0.000122, 0.001384, 0.033880, 0.365964,
    0.000120, 0.002099, 0.014596, 0.358367, 4.368300,
    0.001878, 0.034382, 0.297085, 4.358940, 50.349940,
    0.036969, 0.404663, 3.325891, 44.216007
]
tiempos_columna_iter2 = [
    0.000013, 0.000117, 0.001473, 0.033767, 0.365118,
    0.000121, 0.002129, 0.015277, 0.356621, 4.281214,
    0.001846, 0.035493, 0.294156, 4.312034, 50.782350,
    0.033767, 0.397197, 3.298525, 44.389456
]
tiempos_columna_iter3 = [
    0.000011, 0.000123, 0.001533, 0.033810, 0.364377,
    0.000115, 0.001937, 0.019096, 0.356696, 4.208941,
    0.001745, 0.037596, 0.294496, 4.288010, 51.057167,
    0.031833, 0.388473, 3.289276, 44.120070
]

# Crear la gráfica
plt.figure(figsize=(14, 7))

# Graficar los tiempos de ejecución por fila
plt.plot(tamanos_matriz, tiempos_fila_iter1, label='Suma por Fila - Iteración 1', marker='o')
plt.plot(tamanos_matriz, tiempos_fila_iter2, label='Suma por Fila - Iteración 2', marker='o')
plt.plot(tamanos_matriz, tiempos_fila_iter3, label='Suma por Fila - Iteración 3', marker='o')

# Graficar los tiempos de ejecución por columna
plt.plot(tamanos_matriz, tiempos_columna_iter1, label='Suma por Columna - Iteración 1', marker='x')
plt.plot(tamanos_matriz, tiempos_columna_iter2, label='Suma por Columna - Iteración 2', marker='x')
plt.plot(tamanos_matriz, tiempos_columna_iter3, label='Suma por Columna - Iteración 3', marker='x')

# Configurar la gráfica
plt.xlabel('Tamaño de la Matriz')
plt.ylabel('Tiempo de Ejecución (segundos)')
plt.title('Tiempos de Ejecución de Suma por Fila y por Columna')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)

# Mostrar la gráfica
plt.tight_layout()
# plt.show()

# Definir los tamaños de las matrices y los tiempos de ejecución
tamanos_matriz = [
    "100x100", "100x1000", "100x10000", "1000x100", "1000x1000"
]

# Tiempos de ejecución por fila para cada iteración
tiempos_fila_iter1 = [0.000017, 0.000122, 0.000906, 0.000136, 0.001324]
tiempos_fila_iter2 = [0.000016, 0.000098, 0.000955, 0.000137, 0.001282]
tiempos_fila_iter3 = [0.000017, 0.000098, 0.000924, 0.000138, 0.000898]

# Tiempos de ejecución por columna para cada iteración
tiempos_columna_iter1 = [0.000017, 0.000140, 0.001146, 0.000153, 0.001821]
tiempos_columna_iter2 = [0.000017, 0.000114, 0.001076, 0.000148, 0.001346]
tiempos_columna_iter3 = [0.000016, 0.000113, 0.001860, 0.000148, 0.001518]

# Crear la gráfica
plt.figure(figsize=(14, 7))

# Graficar los tiempos de ejecución por fila
plt.plot(tamanos_matriz, tiempos_fila_iter1, label='Suma por Fila - Iteración 1', marker='o')
plt.plot(tamanos_matriz, tiempos_fila_iter2, label='Suma por Fila - Iteración 2', marker='o')
plt.plot(tamanos_matriz, tiempos_fila_iter3, label='Suma por Fila - Iteración 3', marker='o')

# Graficar los tiempos de ejecución por columna
plt.plot(tamanos_matriz, tiempos_columna_iter1, label='Suma por Columna - Iteración 1', marker='x')
plt.plot(tamanos_matriz, tiempos_columna_iter2, label='Suma por Columna - Iteración 2', marker='x')
plt.plot(tamanos_matriz, tiempos_columna_iter3, label='Suma por Columna - Iteración 3', marker='x')

# Configurar la gráfica
plt.xlabel('Tamaño de la Matriz')
plt.ylabel('Tiempo de Ejecución (segundos)')
plt.title('Tiempos de Ejecución de Suma por Fila y por Columna (Forma Estática)')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)

# Mostrar la gráfica
plt.tight_layout()
plt.show()