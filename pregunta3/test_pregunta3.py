import pytest
from pregunta3 import *
def setup_module(module):
    # Setup some atomic values
    crearAtomico('int', 4, 4)
    crearAtomico('char', 1, 1)
    crearAtomico('double', 8, 8)
    # Setup some structures
    crearStruct('simple_struct', 'int', 'char')
    crearStruct('union1', 'int', 'char')
    crearStruct('nested_struct', 'simple_struct', 'double')

    describir('nested_struct')


def test_error_union():
    fail = crearUnion('union1', 'int', 'char', 'algo')
    assert fail == None
    
    fail2 = crearUnion('union1', 'int', 'char')
    assert fail2 == None

def test_obtener_tamaño_nested_union():
    estructura = Union('union1', 'simple_struct', 'char')
    tamaño, desperdicio = estructura.obtener_tamaño(1)
    assert tamaño == 5
    assert desperdicio == 0

def test_obtener_tamaño_union():
    estructura = Union('union1', 'int', 'char')
    tamaño, desperdicio = estructura.obtener_tamaño(1)
    assert tamaño == 4
    assert desperdicio == 0
    
def test_obtener_alineacion_union():
    estructura = Union('union1', 'int', 'char', 'double')
    assert estructura.obtener_alineacion() == 8

def test_error_struct():
    fail1 = crearStruct('struct1', 'int', 'char', 'fail1')
    assert fail1 == None
    
    fail2 = crearStruct('simple_struct', 'int', 'char')
    assert fail2 == None
    
def test_obtener_tamaño_empaquetado():
    estructura = Estructura('test_struct', 'int', 'char', 'double')
    assert estructura.obtener_tamaño_empaquetado() == 13

def test_obtener_tamaño_sin_empaquetar():
    estructura = Estructura('test_struct', 'int', 'char', 'double')
    memoria, desperdicio = estructura.obtener_tamaño_sin_empaquetar()
    assert len(memoria) == 16
    assert desperdicio == 3

def test_obtener_tamaño_reordenado():
    estructura = Estructura('test_struct', 'int', 'char', 'double')
    memoria, desperdicio = estructura.obtener_tamaño_reordenado()
    assert len(memoria) == 16
    assert desperdicio == 3

def test_obtener_alineacion():
    estructura = Estructura('test_struct', 'int', 'char', 'double')
    assert estructura.obtener_alineacion() == 4

def test_nested_struct_obtener_tamaño_empaquetado():
    estructura = estructuras['nested_struct']
    assert estructura.obtener_tamaño_empaquetado() == 13

def test_nested_struct_obtener_alineacion():
    estructura = estructuras['nested_struct']
    assert estructura.obtener_alineacion() == 4