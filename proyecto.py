import random
from datetime import datetime



lista_jugadores = []  
lista_puntajes = []   

def buscar_jugador(nombre):
    """Busca un jugador en la lista sin importar mayúsculas/minúsculas"""
    for i, jugador in enumerate(lista_jugadores):
        if jugador.lower() == nombre.lower():
            return i  # Retorna el índice del jugador
    return -1  # No encontrado

def registrar_o_obtener_jugador(numero_jugador):
    """Registra un nuevo jugador o obtiene uno existente"""
    global lista_jugadores, lista_puntajes
    
    nombre = input(f"Ingrese el nombre del Jugador {numero_jugador}: ").strip()
    while not nombre:
        nombre = input(f"El nombre no puede estar vacio. Ingrese el nombre del Jugador {numero_jugador}: ").strip()
    
    # Buscar si ya existe un jugador con ese nombre (ignorando mayúsculas/minúsculas)
    indice_jugador = buscar_jugador(nombre)
    
    if indice_jugador != -1:
        # Jugador existente
        jugador_existente = lista_jugadores[indice_jugador]
        puntaje_actual = lista_puntajes[indice_jugador]
        print(f"Bienvenido de vuelta, {jugador_existente}!")
        print(f"Tu puntaje global actual: {puntaje_actual}")
        return jugador_existente
    else:
        # Nuevo jugador
        nombre_normalizado = nombre.title()
        lista_jugadores.append(nombre_normalizado)
        lista_puntajes.append(0)  # Puntaje inicial de 0
        print(f"Jugador {nombre_normalizado} registrado exitosamente!")
        return nombre_normalizado

def actualizar_puntaje_jugador(nombre, puntos_ganados):
    """Actualiza el puntaje global del jugador"""
    global lista_jugadores, lista_puntajes
    
    indice_jugador = buscar_jugador(nombre)
    if indice_jugador != -1:
        lista_puntajes[indice_jugador] += puntos_ganados
        print(f"Puntaje de {nombre} actualizado: +{puntos_ganados} puntos (Total: {lista_puntajes[indice_jugador]})")

def mostrar_ranking_completo():
    """Muestra el ranking completo de todos los jugadores"""
    global lista_jugadores, lista_puntajes
    
    if not lista_jugadores:
        print("\nNo hay jugadores registrados aun.")
        return
    
    # Crear lista de tuplas (nombre, puntaje) y ordenar por puntaje descendente
    ranking_tuplas = list(zip(lista_jugadores, lista_puntajes))
    ranking_tuplas.sort(key=lambda x: x[1], reverse=True)
    
    print("\n" + "="*40)
    print("RANKING GENERAL DE JUGADORES")
    print("="*40)
    print(f"{'Pos':<4} {'Jugador':<20} {'Puntaje':<8}")
    print("-"*40)
    
    for i, (nombre, puntaje) in enumerate(ranking_tuplas, 1):
        medalla = "1" if i == 1 else "2" if i == 2 else "3" if i == 3 else " "
        print(f"{medalla:<1} {i:<3} {nombre:<20} {puntaje:<8}")
    
    print("="*40)

def mostrar_puntaje_jugador(nombre):
    """Muestra el puntaje actual de un jugador específico"""
    global lista_jugadores, lista_puntajes
    
    indice_jugador = buscar_jugador(nombre)
    
    if indice_jugador == -1:
        print(f"\nNo se encontro el jugador: {nombre}")
        return
    
    jugador_encontrado = lista_jugadores[indice_jugador]
    puntaje_actual = lista_puntajes[indice_jugador]
    
    print(f"\nINFORMACION DE {jugador_encontrado.upper()}")
    print("="*30)
    print(f"Puntaje global actual: {puntaje_actual}")
    print("="*30)



def mostrar_instrucciones(rondas_totales):
    print("")
    print("=== BIENVENIDO AL JUEGO PAR O IMPAR ===")
    print("Este te ayudara en tu proceso de aprendizaje los temas: LIMITES y DERIVADAS")
    print("Reglas basicas:")
    print("- Cada jugador debe adivinar si el numero sera PAR o IMPAR")
    print("- Si acierta la paridad, gana 1 punto")
    print("- Si falla, responde una pregunta de Verdadero/Falso, respecto a los temas: LIMITES y DERIVADAS")
    print("- Si responde correctamente, gana el punto; si no, no suma")
    print(f"- Se jugaran {rondas_totales} ronda(s) completa(s)")
    print(f"- Cada ronda = ambos jugadores juegan una vez")
    print(f"- Total de turnos: {rondas_totales * 2}")
    print(f"- Gana quien tenga mas puntos al final de las rondas")
    print("--------------------------------------------------")
    print("")


def prediccion(nombre_jugador):
    eleccion = ""
    while eleccion not in ["PAR", "IMPAR"]:
        eleccion = input(f"{nombre_jugador}, elige PAR o IMPAR: ").upper()
    
    num_aleatorio = random.randint(1, 100)  # Cambiado a 1-100 como en el .psc
    print(f"Número aleatorio generado: {num_aleatorio}")
    
    return eleccion, num_aleatorio


def verificar_paridad(eleccion, num_aleatorio, nombre_jugador):
    if (num_aleatorio % 2 == 0 and eleccion == "PAR") or (num_aleatorio % 2 != 0 and eleccion == "IMPAR"):
        print(f"{nombre_jugador} has acertado la paridad! Ganas 1 punto.")
        return True
    else:
        paridad_real = "PAR" if num_aleatorio % 2 == 0 else "IMPAR"
        print(f"{nombre_jugador}, no has acertado. El numero {num_aleatorio} es {paridad_real}.")
        return False


def hacer_pregunta_vf(preguntas, respuestas, justificaciones, total_preguntas):
    punto_ganado = 0
    print("")
    
    indice_pregunta = random.randint(0, total_preguntas - 1)
    print(preguntas[indice_pregunta])
    print("")
    
    respuesta_pregunta = ""
    while respuesta_pregunta not in ["V", "F"]:
        respuesta_pregunta = input("Ingresa tu respuesta (V/F): ").upper()
    
    if respuesta_pregunta == respuestas[indice_pregunta]:
        print("Respuesta CORRECTA! Ganas 1 punto.")
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

def mostrar_menu_principal():
    """Muestra el menú principal del juego"""
    print("\n" + "="*60)
    print("JUEGO PAR O IMPAR - LIMITES Y DERIVADAS")
    print("="*60)
    print("1. Jugar nueva partida")
    print("2. Ver ranking completo")
    print("3. Ver puntaje de un jugador")
    print("4. Salir")
    print("="*60)

def elegir_numero_rondas():
    """Permite al usuario elegir el número de rondas a jugar"""
    print("\n" + "="*50)
    print("CONFIGURACION DE LA PARTIDA")
    print("="*50)
    print("NOTA: Una ronda = ambos jugadores juegan una vez cada uno")
    
    while True:
        try:
            rondas = int(input("Ingrese el numero de rondas a jugar (1-10): "))
            if 1 <= rondas <= 10:
                print(f"Perfecto! Se jugaran {rondas} ronda(s) = {rondas * 2} turnos totales")
                return rondas
            else:
                print("Por favor ingrese un numero entre 1 y 10.")
        except ValueError:
            print("Por favor ingrese un numero valido.")

def jugar_partida():
    """Función principal para jugar una partida completa"""
    # Elegir número de rondas
    rondas_totales = elegir_numero_rondas()
    
    # Mostrar instrucciones
    mostrar_instrucciones(rondas_totales)
    
    # Registrar jugadores
    print("="*50)
    print("REGISTRO DE JUGADORES")
    print("="*50)
    
    nombre_jugador1 = registrar_o_obtener_jugador(1)
    nombre_jugador2 = registrar_o_obtener_jugador(2)
    
    # Inicializar puntos y contadores
    puntos_jugador1 = 0
    puntos_jugador2 = 0
    ronda_actual = 1
    turno_en_ronda = 1  # 1 para jugador1, 2 para jugador2 en la ronda actual
    
    print(f"\nQue comience la partida entre {nombre_jugador1} y {nombre_jugador2}!")
    input("Presiona ENTER para comenzar...")
    
    # Bucle principal del juego
    while ronda_actual <= rondas_totales:
        # Determinar jugador actual
        if turno_en_ronda == 1:
            nombre_actual = nombre_jugador1
            nombre_oponente = nombre_jugador2
        else:
            nombre_actual = nombre_jugador2
            nombre_oponente = nombre_jugador1
        
        print(f"\n{'='*60}")
        print(f"RONDA {ronda_actual}/{rondas_totales} - TURNO DE {nombre_actual.upper()}")
        print(f"{nombre_jugador1}: {puntos_jugador1} pts | {nombre_jugador2}: {puntos_jugador2} pts")
        print("="*60)
        
        # El jugador hace su predicción
        eleccion, num_aleatorio = prediccion(nombre_actual)
        
        # Verificar si acertó la paridad
        acerto = verificar_paridad(eleccion, num_aleatorio, nombre_actual)
        
        if acerto:
            # Si acertó, gana 1 punto directamente
            if turno_en_ronda == 1:
                puntos_jugador1 += 1
            else:
                puntos_jugador2 += 1
        else:
            # Si falló, debe responder una pregunta
            print(f"\n{nombre_actual}, debes responder una pregunta para ganar el punto:")
            puntos = hacer_pregunta_vf(preguntas, respuestas, justificaciones, total_preguntas)
            if turno_en_ronda == 1:
                puntos_jugador1 += puntos
            else:
                puntos_jugador2 += puntos
        
        # Mostrar puntos actualizados
        print(f"\nPuntos actualizados:")
        print(f"   {nombre_jugador1}: {puntos_jugador1} puntos")
        print(f"   {nombre_jugador2}: {puntos_jugador2} puntos")
        
        # Cambiar de turno dentro de la ronda
        if turno_en_ronda == 1:
            turno_en_ronda = 2
        else:
            # Ronda completa, pasar a la siguiente
            turno_en_ronda = 1
            ronda_actual += 1
        
        # Pausa antes del siguiente turno
        if ronda_actual <= rondas_totales:
            input("\nPresiona ENTER para continuar...")
        else:
            input("\nPresiona ENTER para ver los resultados finales...")
    
    # Determinar ganador y actualizar estadísticas
    print("\n" + "="*60)
    print("JUEGO TERMINADO!")
    print("="*60)
    
    # Determinar ganador por mayor puntaje
    if puntos_jugador1 > puntos_jugador2:
        ganador = nombre_jugador1
        puntos_ganador = puntos_jugador1
        perdedor = nombre_jugador2
        puntos_perdedor = puntos_jugador2
        print(f"{ganador.upper()} HA GANADO con {puntos_ganador} puntos!")
    elif puntos_jugador2 > puntos_jugador1:
        ganador = nombre_jugador2
        puntos_ganador = puntos_jugador2
        perdedor = nombre_jugador1
        puntos_perdedor = puntos_jugador1
        print(f"{ganador.upper()} HA GANADO con {puntos_ganador} puntos!")
    else:
        # Empate
        print("EMPATE!")
        print(f"Ambos jugadores terminaron con {puntos_jugador1} puntos")
        ganador = None
        
    # Actualizar puntajes globales
    actualizar_puntaje_jugador(nombre_jugador1, puntos_jugador1)
    actualizar_puntaje_jugador(nombre_jugador2, puntos_jugador2)
    
    # Mostrar resultado final
    print(f"\nPuntaje final:")
    if ganador:
        print(f"   1ro {ganador}: {puntos_ganador} puntos")
        print(f"   2do {perdedor}: {puntos_perdedor} puntos")
    else:
        print(f"   {nombre_jugador1}: {puntos_jugador1} puntos")
        print(f"   {nombre_jugador2}: {puntos_jugador2} puntos")
    print("="*60)
    
    # Mostrar ranking actualizado
    input("\nPresiona ENTER para ver el ranking actualizado...")
    mostrar_ranking_completo()




def main():
    """Función principal del programa"""
    while True:
        mostrar_menu_principal()
        
        try:
            opcion = input("Selecciona una opcion (1-4): ").strip()
            
            if opcion == "1":
                jugar_partida()
                
            elif opcion == "2":
                mostrar_ranking_completo()
                input("\nPresiona ENTER para volver al menu...")
                
            elif opcion == "3":
                nombre = input("Ingresa el nombre del jugador: ").strip()
                if nombre:
                    mostrar_puntaje_jugador(nombre)
                else:
                    print("Nombre no valido.")
                input("\nPresiona ENTER para volver al menu...")
                
            elif opcion == "4":
                print("\nGracias por jugar! Hasta la proxima!")
                break
                
            else:
                print("Opcion no valida. Por favor selecciona 1, 2, 3 o 4.")
                input("Presiona ENTER para continuar...")
                
        except KeyboardInterrupt:
            print("\n\nHasta luego!")
            break
        except Exception as e:
            print(f"Error inesperado: {e}")
            input("Presiona ENTER para continuar...")


if __name__ == "__main__":
    main()