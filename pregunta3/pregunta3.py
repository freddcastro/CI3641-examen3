import math
from functools import reduce

def mcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def mcm_lista(numeros):
    return reduce(mcm, numeros)


valores_atomicos = {}

estructuras = {}

uniones = {}

class Atomico:
    """
    Clase que representa un tipo de dato atómico.
    Atributos:
    ----------
    nombre : str
        Nombre del tipo de dato atómico.
    representacion : int
        Tamaño en bytes del tipo de dato atómico.
    alineacion : int
        Alineación en bytes del tipo de dato atómico.
    Métodos:
    --------
    obtener_tamaño():
        Retorna el tamaño en bytes del tipo de dato atómico.
    obtener_alineacion():
        Retorna la alineación en bytes del tipo de dato atómico.
    """
    def __init__(self, nombre, representacion, alineacion):
        self.nombre = nombre
        self.representacion = int(representacion)
        self.alineacion = int(alineacion)
        
    def obtener_tamaño(self):
        return self.representacion
    def obtener_alineacion(self):
        return self.alineacion
    
class Estructura:
    """
    Clase que representa una estructura con varios tipos de datos y proporciona métodos para calcular tamaños y alineaciones.
    Atributos:
    ----------
    nombre : str
        Nombre de la estructura.
    tipos : list
        Lista de tipos de datos que componen la estructura.
    Métodos:
    --------
    obtener_tamaño_empaquetado():
        Calcula el tamaño empaquetado de la estructura.
    obtener_tamaño_sin_empaquetar():
        Calcula el tamaño sin empaquetar de la estructura y el desperdicio de memoria.
    indice_multiplo_mas_cercano(lista, numero):
        Encuentra el índice del múltiplo más cercano a un número en una lista.
    helper(indice, prev_alineacion):
        Ayuda a encontrar el tipo de dato con alineación más cercana a una alineación previa.
    intercambiar(i, j):
        Intercambia dos tipos de datos en la lista de tipos.
    obtener_tamaño_reordenado():
        Calcula el tamaño de la estructura reordenando los tipos de datos para minimizar el desperdicio de memoria.
    obtener_alineacion():
        Obtiene la alineación del primer tipo de dato en la lista de tipos.
    """
    def __init__(self, nombre, *tipos):
        self.nombre = nombre
        self.tipos = list(tipos)
        
    def obtener_tamaño_empaquetado(self):
        tamaño = 0
        for tipo in self.tipos:
            if tipo in valores_atomicos:
                tamaño += valores_atomicos[tipo].obtener_tamaño()
            if tipo in estructuras:
                tamaño += estructuras[tipo].obtener_tamaño_empaquetado()
            if tipo in uniones:
                tamaño += uniones[tipo].obtener_tamaño()
        return tamaño
    
    def obtener_tamaño_sin_empaquetar(self):
        memoria = []
        prev_alineacion = 0
        desperdicio = 0
        for tipo in self.tipos:
            if tipo in valores_atomicos:
                representacion_actual = valores_atomicos[tipo].obtener_tamaño()
                alineacion_actual = valores_atomicos[tipo].obtener_alineacion()
                if prev_alineacion % alineacion_actual != 0:
                    for i in range(alineacion_actual - prev_alineacion % alineacion_actual):
                        memoria.append(None)
                
                for i in range(representacion_actual):
                    memoria.append(representacion_actual)
                diferencia = alineacion_actual - representacion_actual
                for i in range(diferencia):
                    memoria.append(None)
                    
                prev_alineacion += alineacion_actual
            if tipo in estructuras:
                memoria, desperdicio1 = estructuras[tipo].obtener_tamaño_sin_empaquetar()
                desperdicio += desperdicio1
            if tipo in uniones:
                return uniones[tipo].obtener_tamaño()
        desperdicio += memoria.count(None)
        return memoria, desperdicio
    
    def indice_multiplo_mas_cercano(self, lista, numero):
        diferencia_minima = float('inf')
        indice_cercano = None
        
        for indice, n in enumerate(lista):
            if numero % n == 0:
                diferencia = abs(numero - n)
                if diferencia < diferencia_minima:
                    diferencia_minima = diferencia
                    indice_cercano = indice
        
        return indice_cercano
    
    def helper(self, indice, prev_alineacion):
        copia = self.tipos[indice:]
        indice_cercano = self.indice_multiplo_mas_cercano([valores_atomicos[tipo].obtener_alineacion() for tipo in copia], prev_alineacion)

        if indice_cercano is None:
            return None

        return copia[indice_cercano]        
    
    def intercambiar(self,i, j):
        self.tipos[i], self.tipos[j] = self.tipos[j], self.tipos[i]
    
    def obtener_tamaño_reordenado(self):
        memoria = []
        prev_alineacion = 0
        desperdicio = 0
        for i in range(len(self.tipos)):
            if self.tipos[i] in valores_atomicos:
                representacion_actual = valores_atomicos[self.tipos[i]].obtener_tamaño()
                alineacion_actual = valores_atomicos[self.tipos[i]].obtener_alineacion()
                if prev_alineacion % alineacion_actual != 0:
                    for j in range(alineacion_actual - prev_alineacion % alineacion_actual):
                        memoria.append(None)
                
                for k in range(representacion_actual):
                    memoria.append(representacion_actual)
                nuevo_valor = self.helper(i+1, alineacion_actual)
                if nuevo_valor is not None:
                    nuevo_indice = self.tipos.index(nuevo_valor)
                    self.intercambiar(i+1, nuevo_indice)
                    prev_alineacion += alineacion_actual    
                    continue
                
                diferencia = alineacion_actual - representacion_actual
                for m in range(diferencia):
                    memoria.append(None)
                prev_alineacion += alineacion_actual
                
            if self.tipos[i] in estructuras:
                memoria, desperdicio1 = estructuras[self.tipos[i]].obtener_tamaño_sin_empaquetar()
                desperdicio += desperdicio1
            if self.tipos[i] in uniones:
                return uniones[self.tipos[i]].obtener_tamaño()
        desperdicio += memoria.count(None)
        return memoria, memoria.count(None)
    
    def obtener_alineacion(self):
        if self.tipos[0] in valores_atomicos:
            return valores_atomicos[self.tipos[0]].obtener_alineacion()
        if self.tipos[0] in estructuras:
            return estructuras[self.tipos[0]].obtener_alineacion()
        if self.tipos[0] in uniones:
            return estructuras[self.tipos[0]].obtener_alineacion()
    
class Union:
    """
    Clase que representa una unión de tipos.
    Atributos:
    ----------
    nombre : str
        Nombre de la unión.
    tipos : tuple
        Tipos que forman parte de la unión.
    Métodos:
    --------
    obtener_tamaño(cond):
        Calcula el tamaño de la unión dependiendo de la condición dada.
        Parámetros:
            cond (int): Condición para calcular el tamaño (1: empaquetado, 2: sin empaquetar, otro: reordenado).
        Retorna:
            tuple: Tamaño máximo y desperdicio de la unión.
    obtener_alineacion():
        Calcula la alineación de la unión.
        Retorna:
            int: Mínimo común múltiplo de las alineaciones de los tipos en la unión.
    """
    def __init__(self, nombre, *tipos):
        self.nombre = nombre
        self.tipos = tipos
        
    def obtener_tamaño(self, cond):
        tamaño = 0
        desperdicio = 0
        for tipo in self.tipos:
            if tipo in valores_atomicos:
                tamaño = max(tamaño, valores_atomicos[tipo].obtener_tamaño())
            if tipo in estructuras:
                if cond == 1:
                    tamaño = max(tamaño, estructuras[tipo].obtener_tamaño_empaquetado())
                elif cond == 2:
                    new_tamaño, new_desperdicio = estructuras[tipo].obtener_tamaño_sin_empaquetar()
                    tamaño = max(tamaño, len(new_tamaño))
                    desperdicio = max(desperdicio, new_desperdicio)
                else:
                    reord_tamaño, reord_desperdicio = max(tamaño, estructuras[tipo].obtener_tamaño_reordenado())
                    tamaño = max(tamaño, reord_tamaño)
                    desperdicio = max(desperdicio, reord_desperdicio)
            if tipo in uniones:
                tamaño = max(tamaño, uniones[tipo].obtener_tamaño())
            
        return tamaño, desperdicio
    
    def obtener_alineacion(self):
        alineaciones = []
        for tipo in self.tipos:
            if tipo in valores_atomicos:
                alineaciones.append(valores_atomicos[tipo].obtener_alineacion())
            if tipo in estructuras:
                alineaciones.append(estructuras[tipo].obtener_alineacion())
        
        return mcm_lista(alineaciones)

def crearAtomico(nombre, representacion, alineacion):
    """
    Crea un nuevo tipo atómico y lo agrega al diccionario de valores atómicos.

    Parámetros:
        nombre (str): El nombre del tipo atómico.
        representacion (str): La representación del tipo atómico.
        alineacion (int): La alineación del tipo atómico.
    Errores:
        Error: Ya existe un tipo con ese nombre. - Si ya existe un tipo con el nombre dado.
    """
    if nombre in valores_atomicos or nombre in estructuras or nombre in uniones:
        print("Error: Ya existe un tipo con ese nombre.")
    else:
        atomico = Atomico(nombre, representacion, alineacion)
        valores_atomicos[nombre] = atomico
    
def crearStruct(nombre, *tipos):
    """
    Crea una nueva estructura con el nombre y tipos especificados.

    Parámetros:
        nombre (str): El nombre de la nueva estructura.
        *tipos (str): Una lista de tipos que compondrán la estructura.

    Errores:
        Imprime un mensaje de error si alguno de los tipos especificados no existe
        en los valores atómicos, estructuras o uniones.
        Imprime un mensaje de error si ya existe un tipo con el nombre especificado.

    """
    for tipo in tipos:
        if tipo not in valores_atomicos:
            if tipo not in estructuras:
                if tipo not in uniones:
                    print(f"Error: El el tipo {tipo} no existe")
                    return
    if nombre in estructuras or nombre in valores_atomicos or nombre in uniones:
        print("Error: Ya existe un tipo con ese nombre.")
    else:
        estructuras[nombre] = Estructura(nombre, *tipos)

def crearUnion(nombre, *tipos):
    """
    Crea una nueva unión con el nombre y tipos especificados.
    Parámetros:
        nombre (str): El nombre de la nueva unión.
        *tipos: Una lista de tipos que conformarán la unión.
    Prints:
        Error: Si alguno de los tipos especificados no existe en valores_atomicos, estructuras o uniones.
        Error: Si ya existe un tipo con el mismo nombre en uniones, estructuras o valores_atomicos.
    """
    for tipo in tipos:
        if tipo not in valores_atomicos:
            if tipo not in estructuras:
                if tipo not in uniones:
                    print(f"El el tipo {tipo} no existe")
                return
        
    if nombre in uniones or nombre in estructuras or nombre in valores_atomicos:
        print("Error: Ya existe un tipo con ese nombre")
    else:
        uniones[nombre] = Union(nombre, *tipos)
        
        
def descripcion_empaquetando(nombre):
    """
    Imprime la descripción del empaquetado de un elemento dado su nombre.
    Parámetros:
    nombre (str): El nombre del elemento a describir. Puede ser un valor atómico, una estructura o una unión.
    Comportamiento:
    - Si el nombre corresponde a un valor atómico, imprime su representación y alineación.
    - Si el nombre corresponde a una estructura, imprime su tamaño empaquetado, alineación y desperdicio (0 bytes).
    - Si el nombre corresponde a una unión, imprime su tamaño, alineación y desperdicio en bytes.
    """
    print("Empaquetando")
    if nombre in valores_atomicos:
        print(f"El valor atómico de nombre {nombre} tiene una representación de {valores_atomicos[nombre].representacion} y una alineación de {valores_atomicos[nombre].alineacion}")
            
    if nombre in estructuras:
        print(f"La estructura de nombre {nombre} tiene un tamaño de {estructuras[nombre].obtener_tamaño_empaquetado()}, una alineación de {estructuras[nombre].obtener_alineacion()} y un desperdicio de 0 bytes")
        
    if nombre in uniones:
        tamaño, desperdicio = uniones[nombre].obtener_tamaño(1)
        print(f"La union de nombre {nombre} tiene un tamaño de {tamaño}, una alineación de {uniones[nombre].obtener_alineacion()} y un desperdicio de {desperdicio} bytes")
           
        
def descripcion_sin_empaquetar(nombre):
    """
    Imprime la descripción sin empaquetar de un elemento dado su nombre.
    Parámetros:
    nombre (str): El nombre del elemento a describir. Puede ser un valor atómico, una estructura o una unión.
    Comportamiento:
    - Si el nombre corresponde a un valor atómico, imprime su representación y alineación.
    - Si el nombre corresponde a una estructura, imprime su tamaño, alineación y desperdicio en bytes.
    - Si el nombre corresponde a una unión, imprime su tamaño, alineación y desperdicio en bytes.
    """
    print("Sin empaquetar")
    if nombre in valores_atomicos:
        print(f"El valor atómico de nombre {nombre} tiene una representación de {valores_atomicos[nombre].representacion} y una alineación de {valores_atomicos[nombre].alineacion}")
            
    if nombre in estructuras:
        tamaño, desperdicio = estructuras[nombre].obtener_tamaño_sin_empaquetar()
        print(f"La estructura de nombre {nombre} tiene un tamaño de {len(tamaño)}, una alineación de {estructuras[nombre].obtener_alineacion()} y un desperdicio de {desperdicio} bytes")
    
    if nombre in uniones:
        tamaño, desperdicio = uniones[nombre].obtener_tamaño(2)
        print(f"La union de nombre {nombre} tiene un tamaño de {tamaño}, una alineación de {uniones[nombre].obtener_alineacion()} y un desperdicio de {desperdicio} bytes")

def descripcion_reordenando(nombre):
    """
    Imprime información detallada sobre el objeto identificado por 'nombre' en las colecciones
    'valores_atomicos', 'estructuras' y 'uniones'. Dependiendo de la colección a la que pertenezca
    'nombre', se imprimirá su representación, alineación, tamaño y desperdicio de bytes.
    Parámetros:
        nombre (str): El nombre del objeto a buscar en las colecciones.
    """
    print("Reordenando")
    if nombre in valores_atomicos:
        print(f"El valor atómico de nombre {nombre} tiene una representación de {valores_atomicos[nombre].representacion} y una alineación de {valores_atomicos[nombre].alineacion}")
            
    if nombre in estructuras:
        tamaño, desperdicio = estructuras[nombre].obtener_tamaño_reordenado()
        print(f"La estructura de nombre {nombre} tiene un tamaño de {len(tamaño)}, una alineación de {estructuras[nombre].obtener_alineacion()} y un desperdicio de {desperdicio} bytes")
        
    if nombre in uniones:
        tamaño, desperdicio = uniones[nombre].obtener_tamaño(3)
        print(f"La union de nombre {nombre} tiene un tamaño de {tamaño}, una alineación de {uniones[nombre].obtener_alineacion()} y un desperdicio de {desperdicio} bytes")
        
def describir(nombre):
    """
    Describe un tipo de dato dado su nombre.

    Esta función verifica si el nombre proporcionado corresponde a un tipo de dato
    atómico, estructura o unión. Si el tipo no existe, imprime un mensaje de error.
    Si el tipo existe, llama a tres funciones para describir el tipo de dato de 
    diferentes maneras: empaquetando, sin empaquetar y reordenando.

    Parámetros:
        nombre (str): El nombre del tipo de dato a describir.

    """
    if nombre not in valores_atomicos:
        if nombre not in estructuras:
            if nombre not in uniones:
                print("Error: El tipo no existe")
                return
    descripcion_empaquetando(nombre)
    descripcion_sin_empaquetar(nombre)
    descripcion_reordenando(nombre)
    


def main():
    while True:
        accion = input().split(" ")
        if accion[0].upper() == 'SALIR':
            break
        elif accion[0].upper() == 'ATOMICO':
            crearAtomico(*accion[1:])
        elif accion[0].upper() == 'STRUCT':
            crearStruct(accion[1], *accion[2:])
        elif accion[0].upper() == 'UNION':
            crearUnion(accion[1], *accion[2:])
        elif accion[0].upper() == 'DESCRIBIR':
            describir(accion[1])


if __name__ == "__main__":
    main()


 
