#Casos prácticos de depuración

# %%
# 1. Error léxico (nombre mal escrito):
def saludo():
    print("Hola mundo")  # Error corregido: 'print' está correctamente definido

saludo()

# %%
# 2. Error de sintaxis (faltan dos puntos):
def suma(a, b):
    return a + b 

suma(2, 3)

# %%
# 3. Error Semántico
def calcular_promedio(lista):
    return sum(lista) * len(lista)  # Error: lógica incorrecta

numeros = [2, 4, 6, 8]
print("Resultado incorrecto:", calcular_promedio(numeros))

    #Objetivo: Aunque el código es válido, da un resultado incorrecto. Prompt: “¿Este código calcula correctamente el promedio de una lista?”

# %%
# 4. Error en Tiempo de Ejecución
def calcular_promedio(lista):
    """
    Calcula el promedio de una lista de números.
    
    Args:
        lista (list): Lista de números.
    
    Returns:
        float: Promedio de los números en la lista, o None si la lista está vacía.
    """
    if not lista:
        return None  # Maneja el caso de lista vacía
    return sum(lista) / len(lista)

numeros = [2, 4, 6, 8]
print("Promedio:", calcular_promedio(numeros))

    # Objetivo: Provocar un IndexError. Prompt sugerido: “Corrige este error de ejecución para que no falle si el índice está fuera de rango.”

# %%
# 5. Código para refactorización
def operacion(a, b):
    """
    Devuelve True si 'a' es mayor que 'b', de lo contrario False.
    
    Args:
        a (int | float): Primer número.
        b (int | float): Segundo número.
    
    Returns:
        bool: Resultado de la comparación.
    """
    return a > b

operacion(5, 3)
    
    #Objetivo: Mostrar cómo Copilot puede sugerir: return a > b prompt: “¿Cómo puedo simplificar esta función?”
# %%
# Error por falta de importación/modulo no encontrado
import pytest

# %%
