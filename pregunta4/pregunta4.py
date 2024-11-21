import matplotlib.pyplot as plt

# Definir los tamaños de las matrices y los tiempos de ejecución
tamanos_matriz = [
    "100x100", "100x1000", "100x10000", "100x100000", "100x1000000",
    "1000x100", "1000x1000", "1000x10000", "1000x100000", "1000x1000000",
    "10000x100", "10000x1000", "10000x10000", "10000x100000", "10000x1000000",
    "100000x100", "100000x1000", "100000x10000", "100000x100000"
]

# Tiempos de ejecución por fila (promedio de las iteraciones)
tiempos_fila_dinamica = [
    0.000011, 0.000095, 0.001467, 0.015469, 0.154082,
    0.000101, 0.000957, 0.014737, 0.157153, 1.541646,
    0.001181, 0.010014, 0.148634, 1.547460, 15.555999,
    0.010621, 0.096104, 1.483586, 15.297193
]

# Tiempos de ejecución por columna (promedio de las iteraciones)
tiempos_columna_dinamica = [
    0.000011, 0.000122, 0.001384, 0.033880, 0.365964,
    0.000120, 0.002099, 0.014596, 0.358367, 4.368300,
    0.001878, 0.034382, 0.297085, 4.358940, 50.349940,
    0.036969, 0.404663, 3.325891, 44.216007
]

# Crear la gráfica
plt.figure(figsize=(14, 7))

# Graficar los tiempos de ejecución por fila
plt.plot(tamanos_matriz, tiempos_fila_dinamica, label='Suma por Fila', marker='o')

# Graficar los tiempos de ejecución por columna
plt.plot(tamanos_matriz, tiempos_columna_dinamica, label='Suma por Columna', marker='x')

# Configurar la gráfica
plt.xlabel('Tamaño de la Matriz')
plt.ylabel('Tiempo de Ejecución (segundos)')
plt.title('Tiempos de Ejecución de Suma por Fila y por Columna (Forma Dinámica)')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)

# Mostrar la gráfica
plt.tight_layout()
# plt.show()

# Definir los tamaños de las matrices y los tiempos de ejecución
tamanos_matriz = [
    "100x100", "100x1000", "1000x100", "1000x1000"
]

# Tiempos de ejecución por fila para cada iteración
tiempos_fila_iter1 = [0.000011, 0.000098, 0.000095, 0.001154]
tiempos_fila_iter2 = [0.000012, 0.000092, 0.000098, 0.000939]
tiempos_fila_iter3 = [0.000010, 0.000095, 0.000094, 0.000947]

# Tiempos de ejecución por columna para cada iteración
tiempos_columna_iter1 = [0.000012, 0.000131, 0.000101, 0.001599]
tiempos_columna_iter2 = [0.000012, 0.000115, 0.000104, 0.001430]
tiempos_columna_iter3 = [0.000012, 0.000113, 0.000101, 0.001434]

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