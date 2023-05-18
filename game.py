import sqlite3
import platform
import os
import time
import sys
import cli_box
from player import BlackJackPlayer, BlackJackDealer
from database import DBSetup
from config_log import start_logger
from colorama import Fore, Back, init, Style
from rich.console import Console
from rich.table import Table
from rich.theme import Theme

init()

if platform.system() == 'Windows':
    init(autoreset=True)


custom_theme = Theme({'success': 'green', 'error': 'bold red',
                      'others': 'blue underline', 'tie': 'magenta', 'lose_bust': 'purple', 'win': 'orange3'})

console = Console(theme=custom_theme)


def tprint(words):
    for char in words:
        time.sleep(0.005)
        sys.stdout.write(char)
        sys.stdout.flush()


intro_ascii = f"""{Fore.RED}

    )  (                )                      )  
 ( /(  )\    )       ( /(    (      )       ( /(  
 )\())((_)( /(   (   )\())   )\  ( /(   (   )\()) 
((_)\  _  )(_))  )\ ((_)\   ((_) )(_))  )\ ((_)\ 
{Fore.BLUE}| |(_)| |((_)_  ((_)| |(_){Fore.MAGENTA}   | |((_)_  ((_)| |(_) 
{Fore.BLUE}| '_ \| |/ _` |/ _| | / / {Fore.MAGENTA}   | |/ _` |/ _| | / /  
{Fore.BLUE}|_.__/|_|\__,_|\__| |_\_\ {Fore.MAGENTA}  _/ |\__,_|\__| |_\_\  
                           |__/                   
{Style.RESET_ALL}"""


def intro():
    clear_screen()
    tprint(intro_ascii)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def black_jack(dealer, pet_amount, player):
    console.print(f"Black Jack!, You have won {int(pet_amount * 2.5)}$", style='success')
    print(f"{Back.LIGHTWHITE_EX}dealer show his hand{Back.RESET}")
    dealer.show_hand()
    pet_amount = int(pet_amount * 2.5)
    player_win(player, pet_amount)
    reset_both(player, dealer)


def low_on_cards(dealer):
    if len(dealer.black_jack_deck) <= 15:
        dealer.reset_deck()
        dealer.shuffle_cards()
        for i in range(4):
            tprint(f"\r{Fore.LIGHTYELLOW_EX}The dealer is shuffling the cards....{i}{Fore.RESET}")
            time.sleep(1)
        print("\n")
        return True


def take_bet(player):
    clear_screen()
    while True:
        try:
            console.print(cli_box.rounded(f"Money: {player.funds}$"))
            if player.funds == 0:
                console.print(f"You lost all of your money", style='error')
                sys.exit()
            bet = int(input(f"{Back.CYAN}How many chips worth in $$ would you like to bet?{Back.RESET} "))
        except ValueError:
            console.print("Sorry! Please can you type in a number", style="error")
        else:
            if bet > player.funds:
                console.print(f"Your bet can't exceed {player.funds}", style='error')
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


def show_some(player, dealer):
    player.show_over_view()
    player.show_hand()
    dealer.show_over_view(False)
    dealer.show_hand_cover()


def players_table(game_db):
    table = Table(title="All Players")
    table.add_column("Name", justify="right", style="cyan", no_wrap=True)
    table.add_column("Money Won", style="green")
    table.add_column("Money Lost", style="red")

    players = game_db.get_all_user()
    players.sort(key=lambda l: l[0])
    if players:
        for player_name, money_won, money_lost in players:
            table.add_row(f"{player_name.capitalize()}", f"{money_won}", f"{money_lost}")
        console.print(table, style='purple')
    else:
        console.print("No player in the database", style='others')


intro()
game = DBSetup()
players_table(game)
my_logger = start_logger()

user_name = input("What's your name: ")
human = BlackJackPlayer(user_name, 1000)

game.setup_db(human)
name, won, lost = game.get_money(user_name)
print(cli_box.rounded(f"Name: {name}  MoneyWon: {won}  MoneyLost: {lost}"))


def main():
    steve = BlackJackDealer('dealer')
    steve.shuffle_cards()

    while True:
        if not low_on_cards(steve):
            time.sleep(3)
        pet = take_bet(human)

        for _ in range(2):
            hit(human, steve)
            hit(steve, steve)

        show_some(human, steve)

        if human.hand_value == 21:
            black_jack(steve, pet, human)
            continue

        while True:
            if human.hand_value > 21:
                player_bust_lost("player bust")
                break
            if hit_or_stand(human, steve): break
            show_some(human, steve)

        if human.hand_value <= 21:
            while steve.hand_value < 17:
                hit(steve, steve)

            steve.show_over_view(True)
            steve.show_hand()

            if steve.hand_value > 21:
                player_win(human, pet * 2)

            elif steve.hand_value > human.hand_value:
                player_bust_lost("player lost")

            elif steve.hand_value < human.hand_value:
                player_win(human, pet * 2)

            else:
                push(human, pet)

        reset_both(human, steve)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print(f"{Fore.LIGHTCYAN_EX}You gotta run? Ok, cya next time!{Fore.LIGHTWHITE_EX}")
        try:
            game.setup_db(human)
        except sqlite3.Error as error:
            my_logger.exception("Error while working with SQLite")
        finally:
            if game.conn:
                game.conn.close()
                my_logger.info("sqlite connection is closed")
    except Exception:
        my_logger.exception("Unknown error")
