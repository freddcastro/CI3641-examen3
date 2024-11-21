# CI3641-examen3

## Pregunta 1

El lenguage escogido para la implementación es Ballerina.io.

### Pregunta 1.a
1. Tipos de datos:
    - **Tipos básicos**: int, float, decimal, boolean, string, byte. nil (null).
    - **Tipos estructurados**: record, map, array, tuple.
    - **Tipos de colección**: table, stream.
    - **Tipos de unión y tipos opcionales**.
    - **Tipos de función y tipos de servicio**.
  
    Mecanismos para la creación de nuevos tipos:
    - **Records**: Permiten definir tipos de datos estructurados con campos nombrados.
    - **Uniones**: Permiten definir un tipo que puede ser uno de varios tipos.
    - **Tipos definidos por el usuario**: Se pueden crear nuevos tipos utilizando la palabra clave type.
2. Funcionamiento del sistema de tipos de Ballerina
    
    - **Sistema de tipos**: Ballerina utiliza un sistema de tipos estático y estructurado, lo que significa que los tipos se verifican en tiempo de compilación.
    - **Equivalencia de tipos**: Ballerina ofrece 2 maneras de evaluar la equivalencia de sus tipos y expresiones. usar `==` verifica el contenido estructural del objeto al que se hace referencia (por ejemplo, si se comparan dos listas, este operador verifica los elementos internos de cada lista para verificar si son iguales). Ahora, usar `===` verifica la referencia a memoria que hacen los objetos, es decir, que si, nuevamente, se comparan 2 listas con los mismos contenidos, la expresión resultará en false puesto que cada lista hace referencia a una dirección en memoria distinta.
    - **Reglas de compatibilidad**: Ballerina permite la conversión explícita entre tipos compatibles. Los tipos de unión y los tipos opcionales permiten manejar valores de diferentes tipos de manera segura. Más específicamente, en Ballerina la compatibilidad de tipos se identifica considerando la estructura del valor en vez de depender únicamente del nombre del tipo.
    - **Inferencia de tipos**: Ballerina puede inferir tipos en muchas situaciones, usando la palabra reservada `var` para variables locales, lo que reduce la necesidad de repetir las declaraciones de tipos; además, funciona con clases también. (Ejemplo detallado en este ![enlace](https://ballerina.io/learn/language-basics/#type-inference))
3. Ballerina.io, al ser un lenguaje de programación diseñado para la integración de sistemas, ofrece una amplia gama de tipos de datos, desde los primitivos (enteros, flotantes, booleanos) hasta los más complejos como estructuras, uniones y tablas. Sin embargo, también contiene otros tipos de datos pertinentes al uso específico del lenguaje como representaciones a HTTP, Querys, etc. Que no necesariamente representan un álgebra, por lo que depende; si nos enfocamos en el subconjunto que contiene las estructuras necesarias, sí es un algebra, pero al considerar el resto de integraciones dentro del lenguaje, no necesariamente puede serlo.
   - **Tipo Producto**: En Ballerina.io, las estructuras y tuplas representan el tipo producto. Cada campo de una estructura puede verse como una proyección del tipo producto.
   - **Tipo Suma**: Las uniones en Ballerina.io corresponden al tipo suma. Una unión permite que una variable tenga uno de varios tipos posibles. Es similar a un tipo algebraico de datos en lenguajes funcionales.
   - **Tipo Cero (Neutro de la Suma)**: NEl tipo nil en Ballerina actúa como el tipo cero, representando la ausencia de un valor.
   - **Tipo Uno (Neutro del Producto)**: El tipo unit () en Ballerina.io puede considerarse como el tipo uno, ya que representa un valor único y no tiene campos.

