import random

def mostrar_instrucciones(puntos_ganar):
    print("")
    print("=== BIENVENIDO AL JUEGO PAR O IMPAR ===")
    print("Este te ayudara en tu proceso de aprendizaje los temas: LIMITES y DERIVADAS")
    print("Reglas basicas:")
    print("- Cada jugador debe adivinar si el numero sera PAR o IMPAR")
    print("- Si acierta la paridad, gana 1 punto")
    print("- Si falla, responde una pregunta de Verdadero/Falso, respecto a los temas: LIMITES y DERIVADAS")
    print("- Si responde correctamente, gana el punto; si no, no suma")
    print(f"- El primer jugador en llegar a {puntos_ganar} puntos gana el juego")
    print("--------------------------------------------------")
    print("")


def prediccion(num_jugador):
    eleccion = ""
    while eleccion not in ["PAR", "IMPAR"]:
        eleccion = input(f"Jugador {num_jugador}, elige PAR o IMPAR: ").upper()
    
    num_aleatorio = random.randint(1, 10)
    print(f"Número aleatorio generado: {num_aleatorio}")
    
    return eleccion, num_aleatorio


def verificar_paridad(eleccion, num_aleatorio):
    if (num_aleatorio % 2 == 0 and eleccion == "PAR") or (num_aleatorio % 2 != 0 and eleccion == "IMPAR"):
        print("¡Has acertado la paridad! Ganas 1 punto.")
        return True
    else:
        print("No has acertado la paridad.")
        return False


def hacer_pregunta_vf(preguntas, respuestas, justificaciones, total_preguntas):
    punto_ganado = 0
    print("Debes responder una pregunta para ganar el punto:")
    print("")
    
    indice_pregunta = random.randint(0, total_preguntas - 1)
    print(preguntas[indice_pregunta])
    
    respuesta_pregunta = ""
    while respuesta_pregunta not in ["V", "F"]:
        respuesta_pregunta = input("Ingresa tu respuesta (V/F): ").upper()
    
    if respuesta_pregunta == respuestas[indice_pregunta]:
        print("¡Respuesta CORRECTA! Ganas 1 punto.")
        punto_ganado = 1
    else:
        print("Respuesta INCORRECTA. NO ganas el punto.")
        print(f"La respuesta correcta era: {respuestas[indice_pregunta]}")
        print(justificaciones[indice_pregunta])
        print("")
    
    return punto_ganado


# Inicializar preguntas
preguntas = [
    "Si el limite de f(x) cuando x tiende a a existe, entonces la funcion es continua en a (V/F)?",
    "Si lim(x->a) f(x) = L y lim(x->a) g(x) = M, entonces lim(x->a) [f(x)+g(x)] = L+M (V/F)?",
    "Si al acercarse a un punto por derecha y por izquierda los limites son distintos, el limite no existe (V/F)?",
    "El limite de una funcion polinomica siempre existe en todos los numeros reales (V/F)?",
    "El limite de (1/x) cuando x tiende a 0 es igual a 0 (V/F)?",
    "Si el limite de f(x) cuando x->a es infinito, se dice que hay una asintota horizontal (V/F)?",
    "La existencia de un limite lateral derecho garantiza la existencia del limite total (V/F)?",
    "El limite de (1/x) cuando x->+infinito es 1 (V/F)?",
    "El limite de una constante siempre es la misma constante (V/F)?",
    "El limite de (x/x) cuando x->0 es 1 (V/F)?",
    "La derivada de una constante es 0 (V/F)?",
    "La derivada de x^2 es 2x (V/F)?",
    "La derivada representa la pendiente de la tangente a la curva en un punto (V/F)?",
    "Si una funcion es derivable en un punto, entonces tambien es continua en ese punto (V/F)?",
    "Si una funcion es continua en un punto, necesariamente es derivable en ese punto (V/F)?",
    "La derivada de sen(x) es cos(x) (V/F)?",
    "Si la segunda derivada de f(x) > 0 en un intervalo, entonces f(x) es concava hacia arriba en ese intervalo (V/F)?",
    "Si la segunda derivada de f(x) = 0 en un punto, entonces necesariamente hay un punto de inflexion (V/F)?",
    "La derivada de ln(x) es 1/x (V/F)?",
    "Si la primera derivada es positiva en un intervalo, la funcion es decreciente (V/F)?"
]

# Inicializar respuestas
respuestas = ["F", "V", "V", "V", "F", "F", "F", "F", "V", "V", 
              "V", "V", "V", "V", "F", "V", "V", "F", "V", "F"]

# Inicializar justificaciones
justificaciones = [
    "Justificacion: Para continuidad se requiere que f(a) exista y que f(a)=lim f(x). Puede existir el limite y no cumplirse eso.",
    "Justificacion: Linealidad de limites: lim(f+g)=lim f + lim g, si ambos limites existen.",
    "Justificacion: Si los limites laterales difieren, el limite total no existe.",
    "Justificacion: Los polinomios son continuos en R; el limite en un punto existe y coincide con su valor.",
    "Justificacion: Al acercarse a 0, 1/x tiende a ±infinito; no hay limite finito (asintota vertical).",
    "Justificacion: Si lim en x=a es infinito, la asintota es VERTICAL en x=a; las horizontales se estudian para x->±infinito.",
    "Justificacion: Un solo limite lateral no garantiza el limite total; deben existir ambos y ser iguales.",
    "Justificacion: (1/x) tiende a 0 (no a 1) cuando x→+infinito.",
    "Justificacion: El limite de una constante es la misma constante.",
    "Justificacion: x/x esta indefinida en x=0 (forma 0/0). Extendiendo f(x)=1 para x<>0, el limite vale 1, pero la fraccion en 0 es indeterminada.",
    "Justificacion: La derivada de una constante es 0: su pendiente es nula.",
    "Justificacion: Regla de la potencia: d/dx(x^n)=n*x^(n-1); para x^2 da 2x.",
    "Justificacion: La derivada es la pendiente de la tangente (razon de cambio instantanea).",
    "Justificacion: Derivabilidad implica continuidad (no al reves).",
    "Justificacion: Continuidad no implica derivabilidad (ej: |x| continua en 0 pero no derivable en 0).",
    "Justificacion: d/dx[sen(x)] = cos(x).",
    "Justificacion: Si la segunda derivadad de f(x)>0 en un intervalo, la funcion es concava hacia arriba en ese intervalo.",
    "Justificacion: la segunda derivadad de f(a)=0 no garantiza inflexion; debe cambiar la concavidad alrededor de a.",
    "Justificacion: Para x>0, d/dx[ln(x)] = 1/x.",
    "Justificacion: Si la primer derivada de F(x)>0 la funcion es creciente, no decreciente."
]

total_preguntas = len(preguntas)

# PROGRAMA PRINCIPAL
puntos_ganar = 5
puntos_jugador1 = 0
puntos_jugador2 = 0
turno = 1  # Comienza el jugador 1

mostrar_instrucciones(puntos_ganar)

# Bucle principal del juego
while puntos_jugador1 < puntos_ganar and puntos_jugador2 < puntos_ganar:
    print(f"\n--- TURNO DEL JUGADOR {turno} ---")
    print(f"Puntajes actuales - Jugador 1: {puntos_jugador1} | Jugador 2: {puntos_jugador2}")
    print("")
    
    # El jugador hace su predicción
    eleccion, num_aleatorio = prediccion(turno)
    
    # Verificar si acertó la paridad
    acerto = verificar_paridad(eleccion, num_aleatorio)
    
    if acerto:
        # Si acertó, gana 1 punto directamente
        if turno == 1:
            puntos_jugador1 += 1
        else:
            puntos_jugador2 += 1
    else:
        # Si falló, debe responder una pregunta
        puntos = hacer_pregunta_vf(preguntas, respuestas, justificaciones, total_preguntas)
        if turno == 1:
            puntos_jugador1 += puntos
        else:
            puntos_jugador2 += puntos
    
    # Cambiar de turno
    if turno == 1:
        turno = 2
    else:
        turno = 1

# Mostrar ganador
print("\n" + "="*50)
print("¡JUEGO TERMINADO!")
print("="*50)
if puntos_jugador1 >= puntos_ganar:
    print(f"¡EL JUGADOR 1 HA GANADO con {puntos_jugador1} puntos!")
else:
    print(f"¡EL JUGADOR 2 HA GANADO con {puntos_jugador2} puntos!")
print(f"Puntaje final - Jugador 1: {puntos_jugador1} | Jugador 2: {puntos_jugador2}")
print("="*50)