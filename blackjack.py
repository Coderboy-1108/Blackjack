import random

class Card:
    card_values = {
        'Ace': 11, '2': 2, '3': 3, '4': 4, '5': 5,
        '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
        'Jack': 10, 'Queen': 10, 'King': 10
    }

    def __init__(self, suit, rank):
        self.suit = suit.capitalize()
        self.rank = rank
        self.points = self.card_values[rank]

def ascii_version_of_card(*cards):
    suits_symbols = ['♠', '♦', '♥', '♣']
    suits_name = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
    lines = [[] for _ in range(9)]

    for card in cards:
        rank = card.rank[0] if card.rank != '10' else card.rank
        suit = suits_symbols[suits_name.index(card.suit)]

        lines[0].append('┌─────────┐')
        lines[1].append(f'│{rank}{" " if rank != "10" else ""}       │')
        lines[2].append('│         │')
        lines[3].append('│         │')
        lines[4].append(f'│    {suit}    │')
        lines[5].append('│         │')
        lines[6].append('│         │')
        lines[7].append(f'│       {" " if rank != "10" else ""}{rank}│')
        lines[8].append('└─────────┘')

    return '\n'.join([''.join(line) for line in lines])

def ascii_version_of_hidden_card(*cards):
    lines = [['┌─────────┐'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'],
             ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'],
             ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['└─────────┘']]

    hidden_cards = ascii_version_of_card(*cards[1:])
    for index, line in enumerate(hidden_cards.split('\n')):
        lines[index].append(line)

    return '\n'.join([''.join(line) for line in lines])


def get_card_value(card_name):
    return Card.card_values[card_name]

def get_initial_cards():
    user_card1 = Card(random.choice(suits_name), random.choice(cards))
    user_card2 = Card(random.choice(suits_name), random.choice(cards))
    dealer_card1 = Card(random.choice(suits_name), random.choice(cards))
    dealer_card2 = Card(random.choice(suits_name), random.choice(cards))
    return user_card1, user_card2, dealer_card1, dealer_card2

def fix_initial_values(cards_value, cards_list):
    if cards_value > 21 and 'Ace' in cards_list:
        cards_value -= 10
        cards_list.remove('Ace')
    return cards_value

def hitting_split(user_cards):
    player_cards_value = sum(get_card_value(card.rank) for card in user_cards)
    player_cards_value = fix_initial_values(player_cards_value, user_cards)
    num_cards_player = 2

    while True:
        if player_cards_value == 21 and num_cards_player == 2:
                print("You have a natural blackjack in the hand.")
                return player_cards_value

        options = input("Do you want to hit or stand : ").lower()
        if options == "hit":
            num_cards_player += 1
            user_card = Card(random.choice(suits_name), random.choice(cards))
            user_cards.append(user_card)
            player_cards_value += get_card_value(user_card.rank)
            player_cards_value = fix_initial_values(player_cards_value, [card.rank for card in user_cards])
            print(ascii_version_of_card(user_card))
            print(f"Your current value of cards is {player_cards_value}")
            if player_cards_value > 21:
                print(f"Your current value of cards is {player_cards_value}")
                print("Bust!!! You lose this hand")
                return player_cards_value
        elif options == "stand":
            print("This hand is over")
            return player_cards_value
        else:
            print("Enter hit or stand")

def dealer(dealer_cards) :
    dealer_cards_value = sum(get_card_value(card.rank) for card in dealer_cards)
    dealer_cards_value = fix_initial_values(dealer_cards_value, dealer_cards)
    num_cards_dealer = 2

    while True:
        if dealer_cards_value == 21 and num_cards_dealer == 2:
            print("Dealer's hole card : ")
            print(ascii_version_of_card(dealer_cards[0]))
            print(f"Dealer's current value of cards is {dealer_cards_value}")
            return  dealer_cards_value

        print("Dealer's hole card : ")
        print(ascii_version_of_card(dealer_cards[0]))
        print(f"Dealer's current value of cards is {dealer_cards_value}")
        while dealer_cards_value < 17:
            num_cards_dealer += 1
            dealer_card = Card(random.choice(suits_name), random.choice(cards))
            dealer_cards.append(dealer_card)
            dealer_cards_value += get_card_value(dealer_card.rank)
            dealer_cards_value = fix_initial_values(dealer_cards_value, [card.rank for card in dealer_cards])
            print("Dealer hits as value less than 17")
            print(ascii_version_of_card(dealer_card))

        return dealer_cards_value

def result(handValue, dealerHandValue, num) :
    if dealerHandValue > 21:
        print(f"Dealer's value of cards is {dealerHandValue}")
        print(f"Your {num} value of cards is {handValue}")
        print("Dealer Bust!! You win")
        return 1
    elif dealerHandValue == 21:
        if handValue == 21:
            print(f"Dealer's value of cards is {dealerHandValue}")
            print(f"Your {num} value of cards is {handValue}")
            print("Draw!")
            return 0
        else:
            print(f"Dealer's value of cards is {dealerHandValue}")
            print("Dealer got blackjack! Dealer wins!")
            return -1
    else:
        if handValue == 21:
            print(f"Your {num} value of cards is {handValue}")
            print("Blackjack!! You win!")
            return 1
        elif handValue > dealerHandValue:
            print(f"Your {num} value of cards is {handValue}")
            print(f"Dealer's value of cards is {dealerHandValue}")
            print("You win!!")
            return 1
        elif dealerHandValue == handValue:
            print(f"Your {num} value of cards is {handValue}")
            print(f"Dealer's value of cards is {dealerHandValue}")
            print("Draw!")
            return 0
        else:
            print(f"Your {num} value of cards is {handValue}")
            print(f"Dealer's value of cards is {dealerHandValue}")
            print("Dealer wins!!")
            return -1

def play_game_loop_notSplit(user_cards, dealer_cards):
    player_cards_value = sum(get_card_value(card.rank) for card in user_cards)
    dealer_cards_value = sum(get_card_value(card.rank) for card in dealer_cards)

    player_cards_value = fix_initial_values(player_cards_value, user_cards)
    dealer_cards_value = fix_initial_values(dealer_cards_value, dealer_cards)

    num_cards_player = 2
    num_cards_dealer = 2

    while True:
        if player_cards_value == 21 and num_cards_player == 2:
            if dealer_cards_value == 21 and num_cards_dealer == 2:
                print("Dealer's hole card : ")
                print(ascii_version_of_card(dealer_cards[0]))
                print(f"Dealer's current value of cards is {dealer_cards_value}")
                print(f"Your current value of cards is {player_cards_value}")
                print("Both player and dealer have a natural blackjack. It's a tie!")
                return 
            else:
                print("Dealer's hole card : ")
                print(ascii_version_of_card(dealer_cards[0]))
                print(f"Dealer's current value of cards is {dealer_cards_value}")
                print(f"Your current value of cards is {player_cards_value}")
                print("Player has a natural blackjack! Player wins!")
                return 

        options = input("Do you want to hit or stand : ").lower()
        if options == "hit":
            num_cards_player += 1
            user_card = Card(random.choice(suits_name), random.choice(cards))
            user_cards.append(user_card)
            player_cards_value += get_card_value(user_card.rank)
            player_cards_value = fix_initial_values(player_cards_value, [card.rank for card in user_cards])
            print(ascii_version_of_card(user_card))
            print(f"Your current value of cards is {player_cards_value}")
            if player_cards_value > 21:
                print("Dealer's hole card : ")
                print(ascii_version_of_card(dealer_cards[0]))
                print(f"Dealer's current value of cards is {dealer_cards_value}")
                print(f"Your current value of cards is {player_cards_value}")
                print("Bust!!! You lose")
                return 
        
        elif options == "stand":
            print("Dealer's hole card : ")
            print(ascii_version_of_card(dealer_cards[0]))

            while dealer_cards_value < 17:
                num_cards_dealer += 1
                dealer_card = Card(random.choice(suits_name), random.choice(cards))
                dealer_cards.append(dealer_card)
                dealer_cards_value += get_card_value(dealer_card.rank)
                dealer_cards_value = fix_initial_values(dealer_cards_value, [card.rank for card in dealer_cards])
                print("Dealer hits as value less than 17")
                print(ascii_version_of_card(dealer_card))

            result(player_cards_value, dealer_cards_value, "current")
            return
        else:
            print("Enter hit or stand")

def main():
    user_cards = [Card(random.choice(suits_name), random.choice(cards)) for _ in range(2)]
    dealer_cards = [Card(random.choice(suits_name), random.choice(cards)) for _ in range(2)]
    
    print("Your Cards : ")
    print(ascii_version_of_card(*user_cards))
    print("Dealer's Cards")
    print(ascii_version_of_hidden_card(*dealer_cards))

    if user_cards[0].rank == user_cards[1].rank:
        while True :
            ans = input("Do you want to split your cards, you can only do it once(y/n) : ").lower()
            if ans == "y" :
                newCard1 = Card(random.choice(suits_name), random.choice(cards))
                user_cards_pair1 = [user_cards[0], newCard1]

                newCard2 = Card(random.choice(suits_name), random.choice(cards))
                user_cards_pair2 = [user_cards[1], newCard2]

                print("First you play your first hand : ")
                print("Your Cards : ")
                print(ascii_version_of_card(*user_cards_pair1))
                print("Dealer's Cards")
                print(ascii_version_of_hidden_card(*dealer_cards))
                firstHandValue = hitting_split(user_cards_pair1)

                print("Now you play your second hand : ")
                print("Your Cards : ")
                print(ascii_version_of_card(*user_cards_pair2))
                print("Dealer's Cards")
                print(ascii_version_of_hidden_card(*dealer_cards))
                secondHandValue = hitting_split(user_cards_pair2)

                dealerCardsValue = dealer(dealer_cards)
                firstHand = result(firstHandValue, dealerCardsValue, "first")
                secondHand = result(secondHandValue, dealerCardsValue, "second")

                if firstHand == 1 and secondHand == 1 :
                    print("As you won both your hands, you win the match!!")
                elif (firstHand == 1 and secondHand == 0) or (firstHand == 0 and secondHand == 1) :
                    print("One hand was a tie. another you won so you win!!")
                elif firstHand == 0 and secondHand == 0:
                    print("Both hands tied, so draw!")
                elif (firstHand == 1 and secondHand == -1) or (firstHand == -1 and secondHand == 1) :
                    print("As you lost one hand and won another hand, It is a Draw!")
                elif (firstHand == -1 and secondHand == 0) or (firstHand == 0 and secondHand == -1) :
                    print("As you lost one hand and another one was a tie, you lost")
                else :
                    print("As you lost both hands, you lose!")
                break
            elif ans == "n" :
                play_game_loop_notSplit(user_cards, dealer_cards)
                break
            else :
                print("Enter y or n")
    else :
        play_game_loop_notSplit(user_cards, dealer_cards)


if __name__ == "__main__":
    suits_name = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
    cards = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen', 'King']
    main()


