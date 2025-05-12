#Casos prácticos de depuración

# %%
# 1. Error léxico (nombre mal escrito):
def saludo():
    prin("Hola mundo")  # Error corregido: 'print' está correctamente definido

saludo()

# %%
# 2. Error de sintaxis (faltan dos puntos):
def suma(a, b)
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
def obtener_elemento(lista):
    return lista[10]  # Puede lanzar IndexError si la lista es muy corta

obtener_elemento([1, 2, 3])

    # Objetivo: Provocar un IndexError. Prompt sugerido: “Corrige este error de ejecución para que no falle si el índice está fuera de rango.”

# %%
# 5. Código para refactorización
def operacion(a, b):
    if a > b:
        return True
    else:
        return False
    
operacion(5, 3)
    
    #Objetivo: Mostrar cómo Copilot puede sugerir: return a > b prompt: “¿Cómo puedo simplificar esta función?”
# %%
# Error por falta de importación/modulo no encontrado
import pytest

# %%
