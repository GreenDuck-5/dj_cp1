# DJ, 1st, Text Based Adventure
import time as t
import random as r
import os
from collections import Counter
from itertools import combinations

phoenix_brooks = {
	"Health": int(25),
	"Morale": int(10),
	"Honor": int(15),
	"Money": int(100),
}

availible_weapons = ("Fist", "Pistol", "Boot")

items = ()

saloon_visited = False
inn_visited = False
casino_visited = False
mine_visited = False
station_visited = False
bank_visited = False
store_visited = False
jail_visited = False
shooting_range_visited = False

saloon_fight = False
jail_break = False

dead = False

times_casino_visited = 0

bartender = "Alive"
old_man = "Alive"


fist = {
    "Damage": 5,
    "Range": 1,
    "Accuracy": {
        "Upper Body": {
            "Head": 60,
            "Right Shoulder": 80,
            "Left Shoulder": 80,
            "Throat": 50,
            "Chest": 95,
            "Stomach": 90
        },
        "Lower Body": {
            "Right Thigh": 40,
            "Left Thigh": 40,
            "Right Shin": 20,
            "Left Shin": 20,
            "Left Foot": 5,
            "Right Foot": 5
        }
    }
}

pistol = {
    "Damage": 20,
    "Range": 45,
    "Accuracy": {
        "Upper Body": {
            "Head": 70,
            "Right Shoulder": 80,
            "Left Shoulder": 80,
            "Throat": 45,
            "Chest": 95,
            "Stomach": 80
        },
        "Lower Body": {
            "Right Thigh": 20,
            "Left Thigh": 20,
            "Right Shin": 10,
            "Left Shin": 10,
            "Left Foot": 30,
            "Right Foot": 30
        }
    }
}

rifle = {
    "Damage": 20,
    "Range": 1375,
    "Accuracy": {
        "Upper Body": {
            "Head": 70,
            "Right Shoulder": 80,
            "Left Shoulder": 80,
            "Throat": 45,
            "Chest": 95,
            "Stomach": 80
        },
        "Lower Body": {
            "Right Thigh": 20,
            "Left Thigh": 20,
            "Right Shin": 10,
            "Left Shin": 10,
            "Left Foot": 30,
            "Right Foot": 30
        }
    }
}

shotgun = {
    "Damage": 30,
    "Range": 90,
    "Accuracy": {
        "Upper Body": {
            "Head": 95,
            "Right Shoulder": 90,
            "Left Shoulder": 90,
            "Throat": 90,
            "Chest": 95,
            "Stomach": 90
        },
        "Lower Body": {
            "Right Thigh": 50,
            "Left Thigh": 50,
            "Right Shin": 10,
            "Left Shin": 10,
            "Left Foot": 30,
            "Right Foot": 30
        }
    }
}

boot = {
    "Damage": 10,
    "Range": 1.5,
    "Accuracy": {
        "Upper Body": {
            "Head": 10,
            "Right Shoulder": 15,
            "Left Shoulder": 15,
            "Throat": 10,
            "Chest": 15,
            "Stomach": 50
        },
        "Lower Body": {
            "Right Thigh": 70,
            "Left Thigh": 70,
            "Right Shin": 90,
            "Left Shin": 90,
            "Left Foot": 95,
            "Right Foot": 95
        }
    }
}

def slots():
    def clear_screen():
        if os.name == 'nt':
            os.system('CLS')
        else:
            os.system('clear')

    def spin_grid():
        symbols = ['C', 'W', 'L', 'A', 'S']
        return [[r.choice(symbols) for _ in range(3)] for _ in range(3)]

    def print_grid(grid):
        print("*************")
        for row in grid:
            print("  ", " | ".join(row))
        print("*************")

    def get_payout(grid, bet):
        payout = 0

        for row in grid:
            if row[0] == row[1] == row[2]:
                payout += symbol_multiplier(row[0]) * bet

        if grid[0][0] == grid[1][1] == grid[2][2]:
            payout += symbol_multiplier(grid[0][0]) * bet
        if grid[0][2] == grid[1][1] == grid[2][0]:
            payout += symbol_multiplier(grid[0][2]) * bet

        return payout

    def symbol_multiplier(symbol):
        if symbol == 'C':
            return 3
        elif symbol == 'W':
            return 4
        elif symbol == 'L':
            return 5
        elif symbol == 'A':
            return 10
        elif symbol == 'S':
            return 20
        return 0

    def slots_main():
        print("Welcome to slots!")
        print("Symbols: C W L A S")

        while phoenix_brooks['Money'] > 0:
            print(f"\nCurrent money: ${phoenix_brooks['Money']}")
            
            bet = input("Place your bet amount: $")
            
            if not bet.isdigit():
                print("Please enter a valid input.")
                continue

            bet = int(bet)

            if bet > phoenix_brooks['Money']:
                print("You don't got that much.")
                continue
            elif bet <= 0:
                print("Bet must be greater than 0.")
                continue

            phoenix_brooks['Money'] -= bet
            print("\nSpinning...\n")
            t.sleep(1)
            grid = spin_grid()
            print_grid(grid)

            payout = get_payout(grid, bet)
            t.sleep(1)
            if payout > 0:
                print(f"You won ${payout}!")
                phoenix_brooks['Money'] += payout
            else:
                print("You lost.")

            if phoenix_brooks['Money'] == 0:
                print("\nNo more money!")
                break

            play_again = input("Do you want to spin again? (Y/N): ").upper()
            if play_again != 'Y':
                break
            else:
                clear_screen()

        print(f"Game over!")
    slots_main()
    return

def blackjack():
    def create_deck():
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4
        r.shuffle(deck)
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
            while phoenix_brooks["Money"] >= 0:
                blackjack_bet = input(f'How much do you want to bet, you have ${phoenix_brooks["Money"]}. Or type \'done\' to exit: $').lower().strip()
                if blackjack_bet == "done":
                    print("Goodbye")
                    return
                elif not blackjack_bet.isdigit():
                    print("Please enter a valid input.")
                    continue
                blackjack_bet = int(blackjack_bet)
                if blackjack_bet > phoenix_brooks["Money"]:
                    print("You don't got that much.")
                    continue
                elif blackjack_bet <= 0:
                    print("Bet must be greater than 0.")
                    continue
                else:
                    phoenix_brooks["Money"] -= blackjack_bet
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
                        phoenix_brooks["Money"] += blackjack_bet*2
                    elif player_total > dealer_total:
                        print("You win!")
                        phoenix_brooks["Money"] += blackjack_bet*2
                    elif player_total < dealer_total:
                        print("Dealer wins.")
                    else:
                        print("It's a tie.")
                        phoenix_brooks["Money"] += blackjack_bet
                    if not play_again():
                        return

    game()
    print(f"You ended with {phoenix_brooks['Money']}")
    return

def poker(phoenix_brooks):
    def clear_screen():
        if os.name == 'nt':
            os.system('CLS')
        else:
            os.system('clear')

    def new_deck():
        return [(r, s) for r in range(2, 15) for s in "SHDC"]

    def card_str(card):
        faces = {11:"J", 12:"Q", 13:"K", 14:"A"}
        rnk,suit = card
        return f"{faces.get(rnk,rnk)}{suit}"

    def evaluate(hand):
        ranks = sorted([c[0] for c in hand], reverse=True)
        suits = [c[1] for c in hand]
        count = Counter(ranks)
        counts = sorted(count.values(), reverse=True)
        flush = len(set(suits))==1
        straight = ranks==list(range(ranks[0], ranks[0]-5,-1))
        if ranks==[14,5,4,3,2]:
            straight=True
            ranks=[5,4,3,2,1]
        if flush and ranks==[14,13,12,11,10]:
            return (10,ranks)
        if flush and straight:
            return (9,ranks)
        if counts==[4,1]:
            return (8,[count.most_common(1)[0][0]])
        if counts==[3,2]:
            return (7,[count.most_common(1)[0][0]])
        if flush:
            return (6,ranks)
        if straight:
            return (5,ranks)
        if counts==[3,1,1]:
            return (4,[count.most_common(1)[0][0]])
        if counts==[2,2,1]:
            pairs = sorted([r for r,c in count.items() if c==2], reverse=True)
            return (3,pairs)
        if counts==[2,1,1,1]:
            return (2,[count.most_common(1)[0][0]])
        return (1,ranks)

    def best_hand(seven):
        best=None
        for five in combinations(seven,5):
            score=evaluate(list(five))
            if best is None or score>best:
                best=score
        return best

    def ai_strength(hand,community):
        combined = hand + community
        if len(combined)<5:
            return max(c[0] for c in combined)
        score = best_hand(combined)
        return score[0]

    def ai_action(player_idx, hand, community, chips, current_bet, to_call, pot, position):
        strength = ai_strength(hand, community)
        stack = chips[player_idx]
        if strength <=2:
            fold_prob,call_prob,raise_prob = 0.5,0.4,0.1
        elif strength <=5:
            fold_prob,call_prob,raise_prob = 0.2,0.6,0.2
        elif strength <=7:
            fold_prob,call_prob,raise_prob = 0.1,0.5,0.4
        else:
            fold_prob,call_prob,raise_prob = 0.0,0.3,0.7
        total=fold_prob+call_prob+raise_prob
        fold_prob/=total
        call_prob/=total
        raise_prob/=total
        rand=r.random()
        if rand<fold_prob:
            return 'fold',0
        elif rand<fold_prob+call_prob:
            bet=min(to_call,stack)
            return 'call',bet
        else:
            low=min(10,stack)
            high=min(40,stack)
            if low>high:
                raise_amount=stack
            else:
                raise_amount=r.randint(low,high)
            return 'raise',raise_amount

    def betting_round(players, active, chips, pot, community, current_bet=0):
        bets=[0]*len(players)
        ai_moves=[]
        while True:
            changed=False
            if active.count(True)==1:
                return pot
            for i in range(len(players)):
                if not active[i]:
                    continue
                to_call=current_bet-bets[i]
                if i==0:
                    clear_screen()
                    print(f"\nYour turn")
                    print(f"Your cards: {' '.join(card_str(c) for c in players[i])}")
                    print(f"Community cards: {' '.join(card_str(c) for c in community)}" if community else "Community cards: None yet")
                    print(f"Pot: {pot} | Your chips: {phoenix_brooks['Money']}")
                    print(f"Current bet: {current_bet}\nTo call: {to_call}\n")
                    if ai_moves:
                        print("AI moves so far this round:")
                        for move in ai_moves:
                            print(move)
                    while True:
                        action=input("check, call, raise, fold: ").lower()
                        if action=="fold":
                            active[i]=False
                            remaining=next((j for j,a in enumerate(active) if a),None)
                            if remaining is not None:
                                if remaining==0:
                                    phoenix_brooks["Money"]+=pot
                                print(f"Player {remaining+1} wins the pot")
                            return pot
                        elif action=="raise":
                            if phoenix_brooks['Money']>=to_call+10:
                                phoenix_brooks['Money']-=to_call+10
                                bets[i]+=to_call+10
                                pot+=to_call+10
                                current_bet+=10
                                changed=True
                                print(f"You raise to {current_bet}")
                                break
                            else:
                                print("Not enough money to raise. Must call or fold.")
                                continue
                        elif action=="call" and to_call>0:
                            if phoenix_brooks['Money']>=to_call:
                                phoenix_brooks['Money']-=to_call
                                bets[i]+=to_call
                                pot+=to_call
                                print("You call")
                                break
                            else:
                                print("Not enough money to call. Must fold.")
                                continue
                        elif action=="check" and to_call==0:
                            print("You check")
                            break
                        else:
                            print("Invalid action. Try again.")
                            continue
                else:
                    position=i
                    action,amount=ai_action(i,players[i],community,chips,current_bet,to_call,pot,position)
                    if action=='fold':
                        active[i]=False
                        move=f"Player {i+1} folds"
                    elif action=='call':
                        chips[i]-=amount
                        bets[i]+=amount
                        pot+=amount
                        move=f"Player {i+1} calls"
                    elif action=='raise':
                        total_raise=to_call+amount
                        if total_raise>chips[i]:
                            total_raise=chips[i]
                        chips[i]-=total_raise
                        bets[i]+=total_raise
                        pot+=total_raise
                        current_bet=max(current_bet,bets[i])
                        changed=True
                        move=f"Player {i+1} raises to {current_bet}"
                    print(move)
                    t.sleep(1)
                    ai_moves.append(move)
            if all(not active[i] or bets[i]==current_bet for i in range(len(players))):
                break
        return pot

    chips=[100]*4
    while phoenix_brooks["Money"]>0 and sum(c>0 for c in chips[1:])>0:
        clear_screen()
        print(f"--- New Hand ---")
        deck=new_deck()
        r.shuffle(deck)
        players=[[deck.pop(),deck.pop()] for _ in range(4)]
        active=[phoenix_brooks["Money"]>0]+[c>0 for c in chips[1:]]
        pot=0
        community=[]
        starting_bet=5
        for i in range(4):
            if active[i]:
                if i==0:
                    phoenix_brooks["Money"]-=starting_bet
                else:
                    chips[i]-=starting_bet
                pot+=starting_bet
        print(f"Your hole cards: {' '.join(card_str(c) for c in players[0])}")
        print(f"Automatic starting bet of {starting_bet} from each player. Pot is {pot}.")
        pot=betting_round(players,active,chips,pot,community)
        if sum(active)==1:
            winner=next((i for i,a in enumerate(active) if a),None)
            if winner is not None:
                if winner==0:
                    phoenix_brooks["Money"]+=pot
                else:
                    chips[winner]+=pot
                print(f"Player {winner+1} wins the pot")
            if input("Start a new hand? (y/n): ").lower()!='y':
                break
            continue
        community=[deck.pop() for _ in range(3)]
        print(f"Flop: {' '.join(card_str(c) for c in community)}")
        pot=betting_round(players,active,chips,pot,community)
        community.append(deck.pop())
        print(f"Turn: {card_str(community[-1])}")
        pot=betting_round(players,active,chips,pot,community)
        community.append(deck.pop())
        print(f"River: {card_str(community[-1])}")
        pot=betting_round(players,active,chips,pot,community)
        results={}
        for i in range(4):
            if active[i]:
                results[i]=best_hand(players[i]+community)
        if results:
            winner=max(results,key=lambda k: results[k])
            if winner==0:
                phoenix_brooks["Money"]+=pot
            else:
                chips[winner]+=pot
            print(f"Player {winner+1} wins the pot")
        print(f"Current money: {phoenix_brooks['Money']}")
        if input("Start a new hand? (y/n): ").lower()!='y':
            break
    print("Poker game over!")

def clear_screen():
    if os.name == 'nt':
        os.system('CLS')
    else:
        os.system('clear')

def introduction(phoenix_brooks):
    print("Old Man: ‘Howdy, Phoenix! Welcome to Ember Bend! It’s a neat little town, at least it was. But that was before the new sheriff came into town, 15 years he’s made this place a living hell. But I’m sure you knew that. That’s why you’re here, Mr. Brooks, no?’")
    t.sleep(1.5)
    while True:
        choice_one = input("1.) Yes. For honor.\n2.) No. For money.\n3.) Yes. For you.\n4.) Shoot him.\n")
        if choice_one == "1":
            print("Phoenix: ‘Of course, only a man with no honor would abandon his home town when it is in need.’")
            t.sleep(1)
            phoenix_brooks["Honor"] += 5
            print("The old man will remember that.")
            t.sleep(1)
            print("Old Man: ‘Atta boy. I raised you right, that’s evident to me.’")
            t.sleep(1)
            break
        elif choice_one == "2":
            print("Phoenix: ‘I am not here for you old man. I am here to make money, and if I stop the sheriff while I'm at it, that’s fine. But it is not my goal.")
            t.sleep(1)
            phoenix_brooks["Honor"] -= 5
            print("The old man will remember that.")
            t.sleep(1)
            break
        elif choice_one == "3":
            print("Phoenix: ‘Yes. I am here for you, my friend. It has been too long. How you been?’")
            t.sleep(1)
            print("Old Man: ‘Thank you.’")
            phoenix_brooks["Morale"] += 5
            print("The old man will remember that.")
            t.sleep(1)
            break
        elif choice_one == "4":
            print("You shoot the old man in the head.")
            t.sleep(1)
            print("He falls to the ground, dead.")
            t.sleep(1)
            old_man = "Dead"
            phoenix_brooks["Honor"] -= 15
            return
        elif choice_one == "skip":
            return
        else:
            print("Please enter valid input.")
            continue
    return

def saloon(phoenix_brooks, saloon_visited, saloon_fight):
    if saloon_visited == False:
        print("You walk up to the saloon, the massive sign at the front reads: ‘The High Noon Saloon’\nYou have seen this building many times, but never in it.\nYou never liked the yelling and crashing.")
        t.sleep(1)
        print("Opening the saloon doors, you can now see what it’s like.\nIt’s loud, but it’s just people having a good time.")
        t.sleep(1)
        print("You walk up to the bartender, asking for a drink.")
        t.sleep(1)
        print("Bartender: ‘5 coins’")
        t.sleep(1)
        while True:
            choice_two = input(f"1.) Pay: You have {phoenix_brooks["Money"]} coins\n2.) Punch him\n3.) Haggle\n4.) Leave\n")
            if choice_two == "1":
                phoenix_brooks["Money"] -= 5
                print("You pay for the drink. It's some good orange juice.\nYou are now fully healed.")
                print("You walk out, feeling satisfied.")
                phoenix_brooks["Health"] = 25
                saloon_visited = True
                return
            elif choice_two == "2":
                saloon_fight = True
                saloon_visited = True
                return
            elif choice_two == "3":
                print("Phoenix: ‘I can do 3’\nBartender: ‘4’")
                while True:
                    choice_three = input("1.) Take the deal\n2.) Leave\n3.) Punch him\n")
                    if choice_three == "1":
                        print("Phoenix: ‘Aight, that works.’")
                        phoenix_brooks["Health"] = 25
                        phoenix_brooks["Money"] -= 4
                        print("You pay for the drink. It's some good orange juice.\nYou are now fully healed.")
                        print("You walk out, feeling satisfied.")
                        saloon_visited = True
                        return
                    elif choice_three == "2":
                        print("Phoenix: ‘Nah, I'll pass.’")
                        print("You leave.")
                        saloon_visited = True
                        return
                    elif choice_three == "3":
                        saloon_fight = True
                        saloon_visited = True
                        return
                    elif choice_three == "4":
                        saloon_visited = True
                        print("You leave.")
                        return
                    else:
                        print("Please enter valid input")
                    continue
            else:
                print("Please enter valid input")
                continue
    elif saloon_visited == True and saloon_fight == False:
        print("Bartender: ‘Welcome back, Phoenix. The usual?’")
    elif saloon_fight == True:
        print("You walk in, the place is destroyed from the tumble you caused.\nThe bartender is there, cleaning up.\nHe spots you walk in.")
        t.sleep(1)
        print("Bartender: ‘YOU! YOU RUINED MY ESTABLISHMENT! HECK YOU!’")
        t.sleep(1)
        print("He runs up to you, punching you in the face.")
        t.sleep(1)
        choice_blerg = input("1.) Apologize and help him\n2.) Punch him back\n3.) Shoot him\n4.) Leave")

def inn(phoenix_brooks):
    print("inn")

def casino(phoenix_brooks):
    print("You walk into the casino. Bright lights, and a heck ton of machines. A few tables as well.")
    while True:
        choice_ugh = input("Where do you want to go?\n1.) Blackjack\n2.) Poker\n3.) Slots\n4.) Quit\n")
        if choice_ugh == "1":
            blackjack()
        if choice_ugh == "2":
            poker(phoenix_brooks)
        elif choice_ugh == "3":
            slots()
        elif choice_ugh == "4":
            return
        clear_screen()
        return

def mine(phoenix_brooks):
    print("mine")

def station(phoenix_brooks):
    print("station")

def bank(phoenix_brooks):
    print("bank")

def store(phoenix_brooks):
    print("store")

def jail(phoenix_brooks):
    print("jail")

def shooting_range(phoenix_brooks):
    print("shooting range")

def sheriff_fight(phoenix_brooks):
    pass

def bandit_fight(phoenix_brooks):
    pass

def bar_fight(phoenix_brooks):
    print("You punch him in the face.")
    print("")

def location_move(phoenix_brooks):
    print("Which would you like you like to go to?")
    print("0.) Check Inventory\n1.) Saloon\n2.) Inn\n3.) Casino\n4.) Mine\n5.) Train Station\n6.) Bank\n7.) General Store\n8.) Jail\n9.) Shooting Range")
    while True:
        new_loc = input().strip()
        if new_loc == "0":
            clear_screen()
            num = 1
            for item in items:
                print(item)
            for weapon in availible_weapons:
                print(f"Weapon #{num}: {weapon}")
                num += 1
            print(f"Money: ${phoenix_brooks['Money']}")
            print(f"Health: {phoenix_brooks['Health']}")
            exit_inventory = input("\nEnter anything to exit inventory:\n")
            if exit_inventory == "anything":
                print("Well you took that literally.")
                t.sleep(2)
                clear_screen()
                break
            else:
                clear_screen()
                break
        elif new_loc == "1":
            clear_screen()
            saloon(phoenix_brooks, saloon_visited, saloon_fight)
            break
        elif new_loc == "2":
            clear_screen()
            inn(phoenix_brooks)
            break
        elif new_loc == "3":
            clear_screen()
            casino(phoenix_brooks)
            break
        elif new_loc == "4":
            clear_screen()
            mine(phoenix_brooks)
            break
        elif new_loc == "5":
            clear_screen()
            station(phoenix_brooks)
            break
        elif new_loc == "6":
            clear_screen()
            bank(phoenix_brooks)
            break
        elif new_loc == "7":
            clear_screen()
            store(phoenix_brooks)
            break        
        elif new_loc == "8":
            clear_screen()
            jail(phoenix_brooks)
            break
        elif new_loc == "9":
            clear_screen()
            shooting_range(phoenix_brooks)
            break
        else:
            print("Please enter valid input.")
            continue

def wild_west_game():
    introduction(phoenix_brooks)
    clear_screen()
    while True:
        location_move(phoenix_brooks)

wild_west_game()