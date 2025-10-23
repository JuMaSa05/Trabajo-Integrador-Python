Funcion mostrarInstrucciones(puntos_ganar)
    Escribir "";
    Escribir "=== BIENVENIDO AL JUEGO PAR O IMPAR ===";
    Escribir "Este te ayudara en tu proceso de aprendizaje los temas: LIMITES y DERIVADAS";
    Escribir "Reglas basicas:";
    Escribir "- Cada jugador debe adivinar si el numero sera PAR o IMPAR";
    Escribir "- Si acierta la paridad, gana 1 punto";
    Escribir "- Si falla, responde una pregunta de Verdadero/Falso, respecto a los temas: LIMITES y DERIVADAS";
    Escribir "- Si responde correctamente, gana el punto; si no, no suma";
    Escribir "- El primer jugador en llegar a ", puntos_ganar, " puntos gana el juego";
    Escribir "--------------------------------------------------";
    Escribir "";
FinFuncion

Funcion resultado <- esPar(numero)
    Definir resultado Como Logico;
    Si numero MOD 2 = 0 Entonces
        resultado <- Verdadero;
    Sino
        resultado <- Falso;
    FinSi
FinFuncion

Funcion prediccion <- leerPrediccion(numero_jugador)
    Definir prediccion Como Caracter;
    Repetir
        Escribir "Jugador ", numero_jugador, " - El numero sera PAR o IMPAR? (Ingrese PAR o IMPAR): ";
        Leer prediccion;
        prediccion <- Mayusculas(prediccion);
    Hasta Que prediccion = "PAR" O prediccion = "IMPAR"
FinFuncion

Funcion num <- generarYMostrarNumero(numero)
    Definir num Como Entero;
    num <- Aleatorio(1, 100);
    Escribir "El numero generado es: ", num;
    Escribir "";
FinFuncion

Funcion punto_ganado <- hacerPreguntaVF(preguntas, respuestas, total_preguntas)
    Definir punto_ganado, indice_pregunta Como Entero;
    Definir respuesta_pregunta Como Caracter;
    
    punto_ganado <- 0;
    Escribir "Debes responder una pregunta para ganar el punto:";
    Escribir "";
    
    indice_pregunta <- Aleatorio(0, total_preguntas - 1);
    Escribir preguntas[indice_pregunta];
    
    Repetir
        Leer respuesta_pregunta;
        respuesta_pregunta <- Mayusculas(respuesta_pregunta);
    Hasta Que respuesta_pregunta = "V" O respuesta_pregunta = "F"
    
    Si respuesta_pregunta = respuestas[indice_pregunta] Entonces
        Escribir "¡Respuesta CORRECTA! Ganas 1 punto.";
        punto_ganado <- 1;
    Sino
        Escribir "Respuesta INCORRECTA. NO ganas el punto.";
        Escribir "La respuesta correcta era: ", respuestas[indice_pregunta];
		
		Segun indice_pregunta Hacer
			0:
				Escribir "Justificacion: Para continuidad se requiere que f(a) exista y que f(a)=lim f(x). Puede existir el limite y no cumplirse eso.";
			1:
				Escribir "Justificacion: Linealidad de limites: lim(f+g)=lim f + lim g, si ambos limites existen.";
			2:
				Escribir "Justificacion: Si los limites laterales difieren, el limite total no existe.";
			3:
				Escribir "Justificacion: Los polinomios son continuos en R; el limite en un punto existe y coincide con su valor.";
			4:
				Escribir "Justificacion: Al acercarse a 0, 1/x tiende a ±infinito; no hay limite finito (asintota vertical).";
			5:
				Escribir "Justificacion: Si lim en x=a es infinito, la asintota es VERTICAL en x=a; las horizontales se estudian para x->±infinito.";
			6:
				Escribir "Justificacion: Un solo limite lateral no garantiza el limite total; deben existir ambos y ser iguales.";
			7:
				Escribir "Justificacion: (1/x) tiende a 0 (no a 1) cuando x?+infinito.";
			8:
				Escribir "Justificacion: El limite de una constante es la misma constante.";
			9:
				Escribir "Justificacion: x/x esta indefinida en x=0 (forma 0/0). Extendiendo f(x)=1 para x<>0, el limite vale 1, pero la fraccion en 0 es indeterminada.";
			10:
				Escribir "Justificacion: La derivada de una constante es 0: su pendiente es nula.";
			11:
				Escribir "Justificacion: Regla de la potencia: d/dx(x^n)=n*x^(n-1); para x^2 da 2x.";
			12:
				Escribir "Justificacion: La derivada es la pendiente de la tangente (razon de cambio instantanea).";
			13:
				Escribir "Justificacion: Derivabilidad implica continuidad (no al reves).";
			14:
				Escribir "Justificacion: Continuidad no implica derivabilidad (ej: |x| continua en 0 pero no derivable en 0).";
			15:
				Escribir "Justificacion: d/dx[sen(x)] = cos(x).";
			16:
				Escribir "Justificacion: Si la segunda derivadad de f(x)>0 en un intervalo, la funcion es concava hacia arriba en ese intervalo.";
			17:
				Escribir "Justificacion: la segunda derivadad de f(a)=0 no garantiza inflexion; debe cambiar la concavidad alrededor de a.";
			18:
				Escribir "Justificacion: Para x>0, d/dx[ln(x)] = 1/x.";
			19:
				Escribir "Justificacion: Si la primer derivada de F(x)>0 la funcion es creciente, no decreciente.";
				
				Escribir "";
		FinSegun
	FinSi
FinFuncion

Funcion puntos_ganados <- procesarJugada(numero, prediccion, preguntas, respuestas, total_preguntas)
    Definir puntos_ganados Como Entero;
    Definir es_numero_par Como Logico;
    
    puntos_ganados <- 0;
    es_numero_par <- esPar(numero);
    
    Si es_numero_par Entonces
        Si prediccion = "PAR" Entonces
            Escribir "¡CORRECTO! El numero es PAR. Ganas 1 punto.";
            puntos_ganados <- 1;
        Sino
            Escribir "¡INCORRECTO! El numero es PAR, no IMPAR.";
            puntos_ganados <- hacerPreguntaVF(preguntas, respuestas, total_preguntas);
        FinSi
    Sino
        Si prediccion = "IMPAR" Entonces
            Escribir "¡CORRECTO! El numero es IMPAR. Ganas 1 punto.";
            puntos_ganados <- 1;
        Sino
            Escribir "¡INCORRECTO! El numero es IMPAR, no PAR.";
            puntos_ganados <- hacerPreguntaVF(preguntas, respuestas, total_preguntas);
        FinSi
    FinSi
FinFuncion

Funcion puntos <- ejecutarTurno(numero_jugador, puntos_p1, puntos_p2, preguntas, respuestas, total_preguntas)
    Definir puntos, numero Como Entero;
    Definir prediccion Como Caracter;
	numero <- 0;
    
    Escribir "";
	Escribir ">>> TURNO DEL JUGADOR ", numero_jugador, " <<<";
	Escribir "Puntos actuales - Jugador 1: ", puntos_p1, " | Jugador 2: ", puntos_p2;
	Escribir "";
    
    prediccion <- leerPrediccion(numero_jugador);
    numero <- generarYMostrarNumero(numero);
    puntos <- procesarJugada(numero, prediccion, preguntas, respuestas, total_preguntas);
FinFuncion

Funcion ganador_encontrado <- verificarGanador(puntos_p1, puntos_p2, puntos_ganar)
    Definir ganador_encontrado Como Logico;
    
    ganador_encontrado <- Falso;
    
    Si puntos_p1 = puntos_p2 Y puntos_p1 = puntos_ganar Entonces
        Escribir "";
        Escribir "===========================================";
        Escribir "¡¡¡LOS JUGADORES HAN EMPATADO!!!";
        Escribir "Puntuacion final - Jugador 1: ", puntos_p1, " | Jugador 2: ", puntos_p2;
        Escribir "===========================================";
        ganador_encontrado <- Verdadero;
    SiNo
        Si puntos_p1 = puntos_ganar Entonces
            Escribir "";
            Escribir "===========================================";
            Escribir "¡¡¡EL JUGADOR 1 HA GANADO EL JUEGO!!!";
            Escribir "Puntuacion final - Jugador 1: ", puntos_p1, " | Jugador 2: ", puntos_p2;
            Escribir "===========================================";
            ganador_encontrado <- Verdadero;
        FinSi
        
        Si puntos_p2 = puntos_ganar Entonces
            Escribir "";
            Escribir "===========================================";
            Escribir "¡¡¡EL JUGADOR 2 HA GANADO EL JUEGO!!!";
            Escribir "Puntuacion final - Jugador 1: ", puntos_p1, " | Jugador 2: ", puntos_p2;
            Escribir "===========================================";
            ganador_encontrado <- Verdadero;
        FinSi
    FinSi
FinFuncion

Funcion continuar_jugando <- preguntarSiJuegaNuevamente(a)
    Definir continuar_jugando Como Logico;
    Definir respuesta Como Caracter;
    
    Escribir '';
    Escribir 'Presione ENTER para continuar.';
    Esperar Tecla;
    Limpiar Pantalla;
    Escribir '¿Desea jugar nuevamente? (s/n)';
    Leer respuesta;
    
    Repetir
        Si Mayusculas(respuesta) = 'S' o Mayusculas(respuesta) = 'N' Entonces
            Si Mayusculas(respuesta) = 'S' Entonces
                continuar_jugando <- Verdadero;
            SiNo
                continuar_jugando <- Falso;
            FinSi
        SiNo
            Escribir 'Respuesta invalida. Porfavor ingrese una de las dos opciones (S o N).';
            Leer respuesta;
        FinSi;
    Hasta Que Mayusculas(respuesta) = 'S' o Mayusculas(respuesta) = 'N';
FinFuncion

// *** NUEVAS FUNCIONES AGREGADAS ***

Funcion ordenarRanking(jugadores, puntos, total)
    Definir i, j, temp_puntos Como Entero;
    Definir temp_jugador Como Cadena;
    
    // Algoritmo de ordenamiento burbuja (orden descendente)
    Para i <- 0 Hasta total-2 Hacer
        Para j <- 0 Hasta total-2-i Hacer
            Si puntos[j] < puntos[j+1] Entonces
                // Intercambiar puntos
                temp_puntos <- puntos[j];
                puntos[j] <- puntos[j+1];
                puntos[j+1] <- temp_puntos;
                
                // Intercambiar jugadores
                temp_jugador <- jugadores[j];
                jugadores[j] <- jugadores[j+1];
                jugadores[j+1] <- temp_jugador;
            FinSi
        FinPara
    FinPara
FinFuncion

Funcion mostrarRanking(jugadores, puntos, total)
    Definir i Como Entero;
    
    Si total > 0 Entonces
        Escribir "";
        Escribir "===========================================";
        Escribir "       RANKING DE PUNTUACIONES";
        Escribir "===========================================";
        Para i <- 0 Hasta total-1 Hacer
            Escribir i+1, ". ", jugadores[i], " - ", puntos[i], " puntos";
        FinPara
        Escribir "===========================================";
        Escribir "";
    FinSi
FinFuncion

// *** FIN DE NUEVAS FUNCIONES ***

Proceso JuegoParImpar
    Definir puntos_p1, puntos_p2, puntos_ganar, total_preguntas, puntos_obtenidos Como Entero;
    Definir continuar, a Como Caracter;
    Definir bool, hay_ganador Como Logico;
    Definir preguntas, respuestas Como Cadena;
    
    // *** NUEVAS VARIABLES PARA EL RANKING ***
    Definir historial_puntos Como Entero;
    Definir historial_jugadores Como Cadena;
    Definir contador_partidas Como Entero;
    Dimension historial_puntos[20];
    Dimension historial_jugadores[20];
    contador_partidas <- 0;
    // *** FIN DE NUEVAS VARIABLES ***
	a<-"";
    puntos_p1 <- 0;
    puntos_p2 <- 0;
    puntos_ganar <- 5;
    total_preguntas <- 20;
    bool <- Verdadero;
    
    Dimension preguntas[20];
    Dimension respuestas[20];
    
    preguntas[0] <- "Si el limite de f(x) cuando x tiende a a existe, entonces la funcion es continua en a (V/F)?";
    respuestas[0] <- "F";
    
    preguntas[1] <- "Si lim(x->a) f(x) = L y lim(x->a) g(x) = M, entonces lim(x->a) [f(x)+g(x)] = L+M (V/F)?";
    respuestas[1] <- "V";
    
    preguntas[2] <- "Si al acercarse a un punto por derecha y por izquierda los limites son distintos, el limite no existe (V/F)?";
    respuestas[2] <- "V";
    
    preguntas[3] <- "El limite de una funcion polinomica siempre existe en todos los numeros reales (V/F)?";
    respuestas[3] <- "V";
    
    preguntas[4] <- "El limite de (1/x) cuando x tiende a 0 es igual a 0 (V/F)?";
    respuestas[4] <- "F";
    
    preguntas[5] <- "Si el limite de f(x) cuando x->a es infinito, se dice que hay una asintota horizontal (V/F)?";
    respuestas[5] <- "F";
    
    preguntas[6] <- "La existencia de un limite lateral derecho garantiza la existencia del limite total (V/F)?";
    respuestas[6] <- "F";
    
    preguntas[7] <- "El limite de (1/x) cuando x->+infinito es 1 (V/F)?";
    respuestas[7] <- "F";
    
    preguntas[8] <- "El limite de una constante siempre es la misma constante (V/F)?";
    respuestas[8] <- "V";
    
    preguntas[9] <- "El limite de (x/x) cuando x->0 es 1 (V/F)?";
    respuestas[9] <- "V";
    
    preguntas[10] <- "La derivada de una constante es 0 (V/F)?";
    respuestas[10] <- "V";
    
    preguntas[11] <- "La derivada de x^2 es 2x (V/F)?";
    respuestas[11] <- "V";
    
    preguntas[12] <- "La derivada representa la pendiente de la tangente a la curva en un punto (V/F)?";
    respuestas[12] <- "V";
    
    preguntas[13] <- "Si una funcion es derivable en un punto, entonces tambien es continua en ese punto (V/F)?";
    respuestas[13] <- "V";
    
    preguntas[14] <- "Si una funcion es continua en un punto, necesariamente es derivable en ese punto (V/F)?";
    respuestas[14] <- "F";
    
    preguntas[15] <- "La derivada de sen(x) es cos(x) (V/F)?";
    respuestas[15] <- "V";
    
    preguntas[16] <- "Si la segunda derivada de f(x) > 0 en un intervalo, entonces f(x) es concava hacia arriba en ese intervalo (V/F)?";
    respuestas[16] <- "V";
    
    preguntas[17] <- "Si la segunda derivada de f(x) = 0 en un punto, entonces necesariamente hay un punto de inflexion (V/F)?";
    respuestas[17] <- "F";
    
    preguntas[18] <- "La derivada de ln(x) es 1/x (V/F)?";
    respuestas[18] <- "V";
    
    preguntas[19] <- "Si la primera derivada es positiva en un intervalo, la funcion es decreciente (V/F)?";
    respuestas[19] <- "F";
    
    mostrarInstrucciones(puntos_ganar);
    
    Repetir
        continuar <- "S";
        Mientras continuar = "S" Hacer
            puntos_obtenidos <- ejecutarTurno(1, puntos_p1, puntos_p2, preguntas, respuestas, total_preguntas);
            puntos_p1 <- puntos_p1 + puntos_obtenidos;
            Escribir "";
            Escribir "Puntos del Jugador 1: ", puntos_p1;
            
            puntos_obtenidos <- ejecutarTurno(2, puntos_p1, puntos_p2, preguntas, respuestas, total_preguntas);
            puntos_p2 <- puntos_p2 + puntos_obtenidos;
            Escribir "";
            Escribir "Puntos del Jugador 2: ", puntos_p2;
            
            hay_ganador <- verificarGanador(puntos_p1, puntos_p2, puntos_ganar);
            Si hay_ganador Entonces
                continuar <- "N";
                
                // *** GUARDAR PUNTOS EN EL HISTORIAL ***
                historial_jugadores[contador_partidas] <- "Jugador 1";
                historial_puntos[contador_partidas] <- puntos_p1;
                contador_partidas <- contador_partidas + 1;
                
                historial_jugadores[contador_partidas] <- "Jugador 2";
                historial_puntos[contador_partidas] <- puntos_p2;
                contador_partidas <- contador_partidas + 1;
                // *** FIN DE GUARDAR PUNTOS ***
            FinSi
            
            Escribir "";
            Escribir "--------------------------------------------------";
        FinMientras
		
		Limpiar Pantalla;
		// *** ORDENAR Y MOSTRAR RANKING ***
		ordenarRanking(historial_jugadores, historial_puntos, contador_partidas);
		mostrarRanking(historial_jugadores, historial_puntos, contador_partidas);
		// *** FIN DE RANKING ***
		
        bool <- preguntarSiJuegaNuevamente(a);
        
        Si bool Entonces
            puntos_p1 <- 0;
            puntos_p2 <- 0;
            Limpiar Pantalla;
            mostrarInstrucciones(puntos_ganar);
        FinSi
    Hasta Que bool = Falso
    
    Limpiar Pantalla;
    Escribir "Gracias por jugar.";
FinProceso