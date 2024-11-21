import ballerina/io;

// Numerales de Church
type Church Cero|Suc;

type Cero record {
    int value = 0;
};

type Suc record {
    Church succesor;
};

function suma(Church a, Church b) returns int{
    // Buscamos el valor interno de a
    int aInt = churchToInt(a);
    // Buscamos el valor interno de b
    int bInt = churchToInt(b);

    return aInt + bInt;
}

function multiplicacion(Church a, Church b) returns int{
    // Buscamos el valor interno de a
    int aInt = churchToInt(a);
    // Buscamos el valor interno de b
    int bInt = churchToInt(b);

    return aInt * bInt;
}

// Función para convertir un numeral de Church a un entero
function churchToInt(Church church) returns int {
    if (church is Cero) {
        return 0;
    } else {
        int value = 1 + churchToInt((<Suc>church).succesor);
        return value;
    }
}

// Numerales de Church

type Persona record {
    string nombre;
    int edad;
};

type PersonaConjunto Persona[];

// Debemos agregar una función que cree un set para nosotros, pues el lenguaje no tiene sets como tipo de datos.
function uniq(PersonaConjunto data) returns PersonaConjunto {
    return 
        from var persona in data 
        group by persona 
        select persona;
}

// Función para obtener la cantidad de personas en el conjunto
function cantidadDePersonas(PersonaConjunto personSet) returns int {
    return personSet.length();
}

// Función para obtener el subconjunto de personas mayores de edad
function mayoresDeEdad(PersonaConjunto personSet) returns PersonaConjunto {
    PersonaConjunto mayores = [];
    foreach var persona in personSet {
        if (persona.edad >= 18) {
            mayores.push(persona);
        }
    }
    return mayores;
}


// Función para obtener el nombre más común en el conjunto
function nombreMasComun(PersonaConjunto personaSet) returns string? {
    map<int> nameCounts = {};
    foreach var persona in personaSet {
        if nameCounts.hasKey(persona.nombre) {
            nameCounts[persona.nombre] = nameCounts[persona.nombre] ?: 0 + 1;
        } else {
            nameCounts[persona.nombre] = 1;
        }
    }

    string? mostCommonName = ();
    int maxCount = 0;
    foreach var [name, count] in nameCounts.entries() {
        if (count > maxCount) {
            maxCount = count;
            mostCommonName = name;
        }
    }
    return mostCommonName;
}

public function main() {
    Church cero = { value: 0 };
    Church uno = <Suc>{succesor: cero};
    Church dos = <Suc>{succesor: uno};
    Church tres = <Suc>{succesor: dos};
    Church cuatro = <Suc>{succesor: tres};
    Church cinco = <Suc>{succesor: cuatro};


    io:println("Suma de 2 y 3: ", suma(dos, tres));
    io:println("multiplicacion de 4 y 5: ", multiplicacion(cuatro, cinco));

    Persona persona1 = {nombre: "Juan", edad: 20};
    Persona persona2 = {nombre: "Pedro", edad: 23};
    Persona persona3 = {nombre: "Juan", edad: 20};
    Persona persona4 = {nombre: "Pedro", edad: 15};
    PersonaConjunto conjunto = [persona1, persona2, persona3, persona4];
    PersonaConjunto conjuntoUnico = uniq(conjunto);
    io:println(conjunto);
    io:println(conjuntoUnico);
    io:println(cantidadDePersonas(conjuntoUnico));
    io:println(mayoresDeEdad(conjuntoUnico));
    io:println(nombreMasComun(conjuntoUnico));


}   