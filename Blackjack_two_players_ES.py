### BLACKJACK (Two Players) ###

from random import randint

cards = ['As', 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():
    # --- INSTRUCCIONES DEL JUEGO ---
    print("\n=== BIENVENIDO AL BLACKJACK DE DOS JUGADORES ===")
    print("\nReglas básicas:")
    print("• Cada jugador empieza con un presupuesto inicial.")
    print("• En cada ronda deben apostar un monto entero positivo menor o igual a su dinero.")
    print("• Se reparten dos cartas a cada jugador y una al dealer.")
    print("• En tu turno, elegí:")
    print("    h -> pedir carta (Hit)")
    print("    s -> plantarte (Stand)")
    print("• Si tu total supera 21, perdés automáticamente (Bust).")
    print("• El dealer pide cartas hasta llegar a 17 o más.")
    print("• Gana quien esté más cerca de 21 sin pasarse.")
    print("• Si empatan, no ganás ni perdés dinero (Push).")
    print("• Al final de cada ronda podés elegir seguir o salir.")
    print("--------------------------------------------------\n")
    # Budgets for each player
    try:
        money_p1 = int(input('Ingrese su presupuesto (Jugador 1):'))
        money_p2 = int(input('Ingrese su presupuesto (Jugador 2):'))
    except ValueError:
        print('\nError: ingrese un número válido.')
        return

    budget_p1 = money_p1
    budget_p2 = money_p2
    stop = ''

    while money_p1 != 0 or money_p2 != 0:
        if stop == 'y':
            # Final balance vs initial
            diff1 = money_p1 - budget_p1
            diff2 = money_p2 - budget_p2
            if diff1 > 0:
                print(f'\nEl Jugador 1 ganó ${diff1}.')
            elif diff1 == 0:
                print('\nEl Jugador 1 quedó igual.')
            else:
                print(f'\nJugador 1 perdió ${-diff1}.')
            if diff2 > 0:
                print(f'El Jugador 2 ganó ${diff2}.')
            elif diff2 == 0:
                print('El Jugador 2 quedó igual.')
            else:
                print(f'Jugador 2 perdió ${-diff2}.')
            break

        # If both are broke, finish
        if money_p1 == 0 and money_p2 == 0:
            print('\nAmbos jugadores se quedaron sin dinero. Fin del juego.')
            break

        # Bets
        # Player 1 bet
        if money_p1 > 0:
            while True:
                try:
                    bet_p1 = int(input('\nJugador 1 - Ingrese su apuesta: '))
                    if bet_p1 <= 0:
                        print('La apuesta debe ser un número positivo.')
                        continue
                    if bet_p1 > money_p1:
                        print("\nNo tiene suficiente dinero (Jugador 1)")
                        continue
                    break
                except ValueError:
                    print('Por favor ingrese un número entero válido.')
            print(f'\nJugador 1 apostó: ${bet_p1}')
        else:
            bet_p1 = 0
            print('\nEl Jugador 1 no tiene dinero para apostar.')

        # Player 2 bet
        if money_p2 > 0:
            while True:
                try:
                    bet_p2 = int(input('\nJugador 2 - Ingrese su apuesta: '))
                    if bet_p2 <= 0:
                        print('La apuesta debe ser un número positivo.')
                        continue
                    if bet_p2 > money_p2:
                        print("\nNo tiene suficiente dinero (Jugador 2)")
                        continue
                    break
                except ValueError:
                    print('Por favor ingrese un número entero válido.')
            print(f'\nJugador 2 apostó: ${bet_p2}')
        else:
            bet_p2 = 0
            print('\nEl Jugador 2 no tiene dinero para apostar.')

        # Hands
        dealer_hand = []
        player1_hand = []
        player2_hand = []

        # First and Second Card (original style)
        def firstTwoCards(hand):
            hand.append(cards[randint(0, len(cards) - 1)])
            if hand[len(hand) - 1] == 10:
                cards.remove(10)

        # Deal first card each
        if money_p1 > 0 and bet_p1 > 0:
            firstTwoCards(player1_hand)
        if money_p2 > 0 and bet_p2 > 0:
            firstTwoCards(player2_hand)
        firstTwoCards(dealer_hand)

        # Deal second card each
        if money_p1 > 0 and bet_p1 > 0:
            firstTwoCards(player1_hand)
        if money_p2 > 0 and bet_p2 > 0:
            firstTwoCards(player2_hand)
        firstTwoCards(dealer_hand)

        # Reveal initial
        print('\nLa casa tiene un', dealer_hand[0])
        if player1_hand:
            print(f'Jugador 1: tiene un {player1_hand[0]} y un {player1_hand[1]}')
        if player2_hand:
            print(f'Jugador 2: tiene un {player2_hand[0]} y un {player2_hand[1]}')

        # Turning 'As' into an integer (original style)
        def asToInt(hand):
            for i in range(0, len(hand)):
                hand[i] = str(hand[i])
            hand.sort()
            if hand.count('As') == 1:
                hand.pop()
                hand.append('11')
            else:
                hand.pop()
                hand.append('11')
                hand.pop(0)
                hand.append('1')
            for i in range(0, len(hand)):
                hand[i] = int(hand[i])

        if 'As' in player1_hand:
            asToInt(player1_hand)
        if 'As' in player2_hand:
            asToInt(player2_hand)
        if 'As' in dealer_hand:
            asToInt(dealer_hand)

        # Hit function (original style and quirks)
        def hit(hand):
            hand.append(cards[randint(0,len(cards)-1)])
            if hand[-1] == 10:
                cards.remove(10)
            if 'As' in hand and sum(hand[:-1]) <= 10:
                try:
                    hand.remove('As')
                except ValueError:
                    pass
                hand.append(11)
            elif 'As' in hand and sum(hand[:-1]) > 10:
                try:
                    hand.remove('As')
                except ValueError:
                    pass
                hand.append(1)

        # --- Player 1 turn ---
        bust_p1 = False
        stand_total_p1 = None
        if player1_hand:
            if sum(player1_hand) == 21:
                print('\nJugador 1: ¡BLACKJACK!')
                stand_total_p1 = 21
            while sum(player1_hand) < 21 and stand_total_p1 is None:
                choice = str(input('\nJugador 1 - ¿Pedir carta (h) o Plantarse (s)? '))
                if choice == 'h':
                    hit(player1_hand)

                    if sum(player1_hand) > 21 and 11 in player1_hand:
                        player1_hand.remove(11)
                        player1_hand.insert(0, 1)

                    if sum(player1_hand) > 21:
                        print(f"\nJugador 1: {sum(player1_hand)}, se pasó de 21 y perdió")
                        bust_p1 = True
                        break
                    else:
                        total_player = sum(player1_hand)
                        print(f"\nJugador 1 recibió un {player1_hand[len(player1_hand)-1]}, Total = {total_player}")
                elif choice == 's':
                    stand_total_p1 = sum(player1_hand)
                    print(f'\nJugador 1 se planta con {stand_total_p1}')
                    break

        # --- Player 2 turn ---
        bust_p2 = False
        stand_total_p2 = None
        if player2_hand:
            if sum(player2_hand) == 21:
                print('\nJugador 2: ¡BLACKJACK!')
                stand_total_p2 = 21
            while sum(player2_hand) < 21 and stand_total_p2 is None:
                choice = str(input('\nJugador 2 - ¿Pedir carta (h) o Plantarse (s)? '))
                if choice == 'h':
                    hit(player2_hand)

                    if sum(player2_hand) > 21 and 11 in player2_hand:
                        player2_hand.remove(11)
                        player2_hand.insert(0, 1)

                    if sum(player2_hand) > 21:
                        print(f"\nJugador 2: {sum(player2_hand)}, se pasó de 21 y perdió")
                        bust_p2 = True
                        break
                    else:
                        total_player = sum(player2_hand)
                        print(f"\nJugador 2 recibió un {player2_hand[len(player2_hand)-1]}, Total = {total_player}")
                elif choice == 's':
                    stand_total_p2 = sum(player2_hand)
                    print(f'\nJugador 2 se planta con {stand_total_p2}')
                    break

        # If both busted, dealer doesn't need to draw; still show dealer hand/result
        # Dealer turn
        if sorted(dealer_hand) == [6, 11]: # Turning a "Soft 17" into a 7 (keeping original quirk)
            dealer_hand.sort()
            dealer_hand.pop()
            dealer_hand.append(1)

        # Dealer hits only if at least one player is still in the game (<=21)
        if (not bust_p1 and player1_hand) or (not bust_p2 and player2_hand):
            while sum(dealer_hand) < 17:
                hit(dealer_hand)

        # Show dealer total
        total_dealer = sum(dealer_hand)
        print(f"\nCartas de la casa: {dealer_hand}  Total = {total_dealer}")

        # Resolve outcomes per player
        # Player 1
        if player1_hand and bet_p1 > 0:
            if sum(player1_hand) > 21:
                print('\nJugador 1 pierde (se pasó de 21).')
                money_p1 -= bet_p1
            else:
                total_player = sum(player1_hand)
                if total_dealer > 21:
                    print('\nLa casa perdió contra el Jugador 1.')
                    money_p1 += bet_p1
                elif total_dealer > total_player:
                    print('\nJugador 1 perdió')
                    money_p1 -= bet_p1
                elif total_dealer < total_player:
                    print('\nJugador 1 ganó.')
                    money_p1 += bet_p1
                else:
                    print('\nJugador 1 empató.')

            print(f'Dinero del Jugador 1 = ${money_p1}')

        # Player 2
        if player2_hand and bet_p2 > 0:
            if sum(player2_hand) > 21:
                print('\nJugador 2 pierde (se pasó de 21).')
                money_p2 -= bet_p2
            else:
                total_player = sum(player2_hand)
                if total_dealer > 21:
                    print('\nLa casa perdió contra el Jugador 2.')
                    money_p2 += bet_p2
                elif total_dealer > total_player:
                    print('\nJugador 2 perdió')
                    money_p2 -= bet_p2
                elif total_dealer < total_player:
                    print('\nJugador 2 ganó.')
                    money_p2 += bet_p2
                else:
                    print('\nJugador 2 empató.')

            print(f'Dinero del Jugador 2 = ${money_p2}')

        # Continue?
        if money_p1 == 0 and money_p2 == 0:
            print('\nAmbos jugadores se quedaron sin dinero. Fin del juego.')
            break
        stop = input('¿Desea salir del juego? (Sí/No): ').strip().lower()
        if stop in ['si', 's']:
             stop = 'y'
        elif stop in ['no', 'n']:
              stop = 'n'

if __name__ == '__main__':
    try:
        blackjack()
    except ValueError:
        print('\nError: ingrese un número válido.')
