### BLACKJACK ###

from random import randint

cards = ['As', 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack(money):
    budget = money
    stop = ''
    while money != 0:
        if stop == 'y':
            if money > budget:
                print(f'\nYou won ${money-budget}.')
                break
            elif money == budget:
                print('\nYou just lost your time.')
                break
            else:
                print(f'\nYou lost ${budget-money}.')
                break
        else:
            pass

        # Bet
        bet = int(input('\nPlace your bet: '))
        while bet > money:
            print('\nyou don\'t have enough money')
            bet = int(input('\nPlace your bet: '))
        print(f'\nYour bet: ${bet}')

        # Start
        dealer_hand = []
        player_hand = []

        # First and Second Card
        def firstTwoCards(hand):
            hand.append(cards[randint(0, len(cards) - 1)])
            if hand[len(hand) - 1] == 10:
                cards.remove(10)

        # First Player Card
        firstTwoCards(player_hand)

        # First Dealer Card
        firstTwoCards(dealer_hand)

        # Second Player Card
        firstTwoCards(player_hand)

        # Second Dealer Card
        firstTwoCards(dealer_hand)

        print('\nThe dealer has a', dealer_hand[0])
        print(f'You have a {player_hand[0]} and a {player_hand[1]}')

        # Turning 'As' into an integer
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

        if 'As' in player_hand:
            asToInt(player_hand)

        if 'As' in dealer_hand:
            asToInt(dealer_hand)

        # Hitting
        def hit(hand):
            hand.append(cards[randint(0,len(cards)-1)])
            if hand[-1] == 10:
                cards.remove(10)
            if 'As' in hand and sum(hand[:-1]) <= 10:
                hand.remove('As')
                hand.append(11)
            elif 'As' in hand and sum(hand[:-1]) > 10:
                hand.remove('As')
                hand.append(1)

        # Player turn
        if sum(player_hand) == 21:
            print('\n¡BLACKJACK!')
            total_player = sum(player_hand)

        while sum(player_hand) < 21:
            choice = str(input('\nHit(h) or Stand(s)? '))
            if choice == 'h':
                hit(player_hand)

                if sum(player_hand) > 21 and 11 in player_hand:
                    player_hand.remove(11)
                    player_hand.insert(0, 1)

                if sum(player_hand) > 21:
                    print(f'\n{sum(player_hand)}, You lost')
                    break
                else:
                    total_player = sum(player_hand)
                    print(f'\nYou received a {player_hand[len(player_hand)-1]}, Total = {total_player}')
            elif choice == 's':
                total_player = sum(player_hand)
                print(f'\nYou stand in {total_player}')
                break

        if sum(player_hand) > 21:
            money -= bet
            print(f'\nMoney = ${money}')
            if money == 0:
                continue
            else:
                stop = str(input('\nDo you want to Leave? Yes(y)/No(n) '))
                continue

        # Dealer turn
        if sorted(dealer_hand) == [6, 11]: # Turning a "Soft 17" into a 7
            dealer_hand.sort()
            dealer_hand.pop()
            dealer_hand.append(1)

        while sum(dealer_hand) < 17:
            hit(dealer_hand)

        if sum(dealer_hand) > 21:
            print(f'\nThe house lost. ({sum(dealer_hand)})')
            money += bet
            print(f'Money = ${money}')
            stop = str(input('\nDo you want to Leave? Yes(y)/No(n) '))
            continue

        total_dealer = sum(dealer_hand)

        if total_dealer == 21:
            print('\nThe dealer has a Blackjack')
        else:
            print(f'\nThe dealer stands in {total_dealer}')

        # The end
        if total_player > total_dealer:
            if len(dealer_hand) == 2 and total_player == 21:
                print('\nYou win.')
                money += bet*(1.5)
            else:
                print('\nYou win.')
                money += bet
        elif total_dealer == total_player:
            print('\nTie.')
        else:
            print('\nYou lost')
            money -= bet

        print(f'\nMoney = ${money}')

        if money == 0:
                continue
        else:
            stop = str(input('\nDo you want to Leave? Yes(y)/No(n) '))
            continue

try:
    blackjack(int(input('Place your budget: ')))
except ValueError:
    print('\nValue Error Occured')