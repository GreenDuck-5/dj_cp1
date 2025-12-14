import os
import random
import time

def clear_screen():
    if os.name == 'nt':
        os.system('CLS')
    else:
        os.system('clear')

def create_deck():
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4
    random.shuffle(deck)
    return deck

def deal_hand(deck, num_cards = 2):
    hand = []
    for _ in range(num_cards):
        card = deck.pop()
        if card == 11: card = "J"
        elif card == 12: card = "Q"
        elif card == 13: card = "K"
        elif card == 14: card = "A"
        hand.append(card)
    return hand

def calculate_total(hand):
    total = 0
    aces = 0
    for card in hand:
        if card in ["J", "Q", "K"]:
            total += 10
        elif card == "A":
            total += 11
            aces += 1
        else:
            total += card
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

def print_hands(player_hand, dealer_hand, reveal_dealer = False):
    if reveal_dealer:
        print(f"Dealer's hand: {dealer_hand} (Total: {calculate_total(dealer_hand)})")
    else:
        print(f"Dealer's showing: {dealer_hand[0]}")
    print(f"Your hand: {player_hand} (Total: {calculate_total(player_hand)})")

def hit(deck, hand):
    card = deck.pop()
    if card == 11: card = "J"
    elif card == 12: card = "Q"
    elif card == 13: card = "K"
    elif card == 14: card = "A"
    hand.append(card)

def check_blackjack(player_hand, dealer_hand):
    player_total = calculate_total(player_hand)
    dealer_total = calculate_total(dealer_hand)
    if player_total == 21:
        print_hands(player_hand, dealer_hand, reveal_dealer=True)
        print("You got a Blackjack!")
        return True
    elif dealer_total == 21:
        print_hands(player_hand, dealer_hand, reveal_dealer=True)
        print("Dealer got a Blackjack. You lose.")
        return True


def play_again():
    choice = input("Do you want to play again? (Y/N): ").strip().lower()
    if choice == 'y': 
        return True

def game():
    while True:
        clear_screen()
        print("Blackjacking time.\n")
        current_deck = create_deck()
        player_hand = deal_hand(current_deck)
        dealer_hand = deal_hand(current_deck)
        print_hands(player_hand, dealer_hand)
        if check_blackjack(player_hand, dealer_hand):
            if not play_again():
                break
            continue
        while True:
            choice = input("Do you want to Hit or Stand:\n").strip().lower()
            if choice == 'hit':
                hit(current_deck, player_hand)
                print_hands(player_hand, dealer_hand)
                if calculate_total(player_hand) > 21:
                    print("You busted! Dealer wins.")
                    break
            elif choice == 'stand':
                break
            else:
                print("Please enter valid input.")
        while calculate_total(dealer_hand) < 17:
            hit(current_deck, dealer_hand)
        clear_screen()
        print_hands(player_hand, dealer_hand, reveal_dealer=True)
        player_total = calculate_total(player_hand)
        dealer_total = calculate_total(dealer_hand)
        if player_total > 21:
            print("You busted!")
        elif dealer_total > 21:
            print("Dealer busted! You win!")
        elif player_total > dealer_total:
            print("You win!")
        elif player_total < dealer_total:
            print("Dealer wins.")
        else:
            print("It's a tie!")
        if not play_again():
            break

game()