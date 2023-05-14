from player import BlackJackPlayer, BlackJackDealer
from colorama import Fore, Back, init
import time
import os
from rich.console import Console
from rich.theme import Theme


init(autoreset=True)

custom_theme = Theme({'success': 'green', 'error': 'bold red',
                      'others': 'blue underline', 'tie': 'magenta', 'lose_bust': 'purple', 'win': 'orange3'})

console = Console(theme=custom_theme)


def intro():
    clear_screen()
    print(
        """┌────────────────────────────────────────┐
         \r│        Black Jack Terminal Game        │
         \r└────────────────────────────────────────┘"""
    )


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def black_jack(dealer, pet_amount, player):
    console.print(f"Black Jack!, You have won {int(pet_amount * 2.5)}$", style='success')
    print(f"{Back.LIGHTWHITE_EX}dealer show his hand{Back.RESET}")
    dealer.show_hand()
    pet_amount = int(pet_amount * 2.5)
    player_win(player, pet_amount)
    reset_both(player, steve)


def low_on_cards():
    if len(steve.black_jack_deck) <= 20:
        steve.reset_deck()
        steve.shuffle_cards()
        for i in range(4):
            print(f"\r{Fore.LIGHTYELLOW_EX}The dealer is shuffling the cards....{i}", end='')
            time.sleep(1.5)
        print("\n")
        return True


def take_bet(player):
    clear_screen()
    while True:
        try:
            bet = int(input(f"{Back.CYAN}How many chips worth in $$ would you like to bet?{Back.RESET} "))
        except ValueError:
            console.print("Sorry! Please can you type in a number", style="error")
        else:
            if bet > player.funds:
                print(f"Your bet can't exceed {player.funds}")
            elif bet < 1:
                console.print("Your bet can't by less than 1$", style="error")
            else:
                try:
                    player.remove_funds(bet)
                except ValueError:
                    console.print('The number you inputted is negative', style="error")
                else:
                    return bet


def hit(hand, dealer):
    hand.add_card(dealer.deal())
    hand.adjust_for_ace()


def hit_or_stand(hand, dealer):
    while True:
        ask = input("Would you like to hit or stand please enter [H]or[S]: ").lower().strip()
        if ask == 'h':
            hit(hand, dealer)
            clear_screen()
        elif ask == 's':
            console.print("player stands, Dealer is playing....", style='others')
            clear_screen()
            return True
        else:
            console.print("Sorry I didn't understand that! please try again!", style='error')
            continue
        break


def player_bust_lost(message):
    console.print(f"👎 {message}", style='lose_bust')


def player_win(player, pets):
    console.print("👍 player win", style='win')
    player.add_funds(pets)


def push(player, pets):
    console.print("🫳 It's a tie", style='tie')
    # it's because I take the pet from the start
    player.add_funds(pets)


def reset_both(player, dealer):
    player.reset()
    dealer.reset()


def show_some():
    human.show_over_view()
    human.show_hand()
    steve.show_over_view(False)
    steve.show_hand_cover()


intro()
human = BlackJackPlayer('hasan', 1000)
steve = BlackJackDealer('dealer')
steve.shuffle_cards()

while True:
    if not low_on_cards():
        time.sleep(3)
    pet = take_bet(human)

    for _ in range(2):
        hit(human, steve)
        hit(steve, steve)

    show_some()

    if human.hand_value == 21:
        black_jack(steve, pet, human)
        continue

    while True:
        if human.hand_value > 21:
            player_bust_lost("player bust")
            break
        if hit_or_stand(human, steve): break
        show_some()

    if human.hand_value <= 21:
        while steve.hand_value < 17:
            hit(steve, steve)

        steve.show_over_view(True)
        steve.show_hand()

        if steve.hand_value > 21:
            player_win(human, pet*2)

        elif steve.hand_value > human.hand_value:
            player_bust_lost("player lost")

        elif steve.hand_value < human.hand_value:
            player_win(human, pet*2)

        else:
            push(human, pet)

    reset_both(human, steve)
