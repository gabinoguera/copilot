#Casos prácticos de depuración

# 1. Error léxico (nombre mal escrito):
def saludo():
    prin("Hola mundo")  # Error: 'prin' no está definido

# 2. Error de sintaxis (falta de paréntesis):
def suma(a, b):
    return a + b  # Error: falta un paréntesis de cierre

# 3. Error Semántico
def calcular_promedio(lista):
    return sum(lista) * len(lista)  # Error: lógica incorrecta

    #Objetivo: Aunque el código es válido, da un resultado incorrecto. Prompt: “¿Este código calcula correctamente el promedio de una lista?”

# 4. Error en Tiempo de Ejecución
def obtener_elemento(lista):
    return lista[10]  # Puede lanzar IndexError si la lista es muy corta

obtener_elemento([1, 2, 3])

    # Objetivo: Provocar un IndexError. Prompt sugerido: “Corrige este error de ejecución para que no falle si el índice está fuera de rango.”

# 5. Código para refactorización
def operacion(a, b):
    if a > b:
        return True
    else:
        return False
    
    #Objetivo: Mostrar cómo Copilot puede sugerir: return a > b prompt: “¿Cómo puedo simplificar esta función?”