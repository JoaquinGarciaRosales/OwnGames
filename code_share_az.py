# Casino vegas
# Nota personal, implementar hacer el type de "rules" para mostrar las reglas
# Nota personal, se puede hacer módulo de la validación inicial pero con ¿Rules?

import random
import os
import math

# Function clear screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Function to continue
def cont():
    while True:
        cont = input("Press ENTER to continue: ")
        if cont == "":
            break

# Function to validate bet
def bet_val(Money):
    while True:
        bet = input(
                "Select the amount of the bet (no limits, and enter a valid amount) or type NO to leave: ")
        if bet == "NO":
            return bet
        if bet.isdigit() and (int(bet) > 0) and (int(bet) <= Money):
            betN = int(bet)
            return betN

# Function to display Final message
def print_state(Money, Score):
    if Money == 0:
        print("\nYou are broke now. Go back home!\n")
        return 0
    elif Money >= Score:
        print("\nYou win, the casino is broke now :(. Now you have: $", Money,"\n")
        return 0
    else:
        print("\nYou managed to get out with: $", Money,"\n")
        cont()
        return 1

# Game UI
def ui(money, score):
    clear()
    while True:
        print(" __________________________________________________________________________________________________________")
        print("|Current Balance: $", money, "     You need to get: ",(score-money), "more      ", "Score needed: $", score,)
        print("|__________________________________________________________________________________________________________\n")
        break

# El más complicado BLACKJACK

# Dictionary
dict_values = {"A": 11, "J": 10, "Q": 10, "K": 10}

# Function to values
def func_values(array):
    aces = 0
    value = 0
    for char in array:
        charN = char[:-1]
        if charN in dict_values:
            value += dict_values[charN]
            if charN == "A":
                aces += 1
        elif charN in {"2", "3", "4", "5", "6", "7", "8", "9", "10"}:
            value += int(charN)
    while value > 21 and aces > 0:
        value -= 10
        aces -= 1
    return value

# Function printer
def func_printer(array, dealer_in):
    for i, char in enumerate(array, start=1):
        if char != "":
            if dealer_in == 1:
                print(f"Dealer card {i}: {char}")
            else:
                print(f"Player card {i}: {char}")
    print("")

# Deck Builder
def build_deck(n_decks):
            suits = ["♠", "♥", "♦", "♣"]
            value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
            baraja = [f"{v}{p}" for p in suits for v in value]
            total_deck = baraja * n_decks
            random.shuffle(total_deck)
            return total_deck

# Main to Blackjack
def blackjack(Money, Score):
    while True:
        decks_in = input(
            "\nSelect the amount of decks you are going to play with (an int between 5 and 8): ")
        if decks_in.isdigit() and 4 < int(decks_in) < 9:
            decks = int(decks_in)
            break
    crafted_deck = build_deck(decks)
    initial_size = len(crafted_deck)
    while Money < Score and Money != 0:
        ui(Money, Score)
        bet = bet_val(Money)
        if bet == "NO":
            return Money
        # Re Shuffle if needed
        if len(crafted_deck) < (initial_size/4):
            print("Casino is running out of cards, we need to reshuffle")
            crafted_deck = build_deck(decks)
        dealer_ar = [""] * 16
        player_ar = [""] * 20
        # Carta dealer
        dealer_ar[0] = crafted_deck.pop()
        # Función imprimir
        print("")
        func_printer(dealer_ar, 1)
        # Primera carta jugador
        player_ar[0] = crafted_deck.pop()
        # Segunda carta jugador
        player_ar[1] = crafted_deck.pop()
        # Función imprimir
        func_printer(player_ar, 0)
        valueP = func_values(player_ar)
        if valueP != 21:
            print("\n1 for hit.\n2 for double.\n3 for stay.\n")
            while True:
                election = input("Hit, double or stay: ")
                if election.isdigit() and (int(election) in (1, 3)):
                    break
                if election.isdigit() and (int(election) == 2):
                    if bet*2 > Money:
                        print("\nNot enough money to double\n")
                    else:
                        break
            action = int(election)
            match action:
                case 1:
                    ui(Money, Score)
                    i = 0
                    while action != 3:
                        print("\n1 for hit.\n3 for stay.\n")
                        player_ar[i+2] = crafted_deck.pop()
                        valueP = func_values(player_ar)
                        print("")
                        func_printer(dealer_ar, 1)
                        func_printer(player_ar, 0)
                        i += 1
                        if valueP >= 21:
                            break
                        else:
                            while True:
                                election = input("Hit(1) or stay(3): ")
                                if election.isdigit() and (int(election) in (1, 3)):
                                    action = int(election)
                                    break
                case 2:
                    bet = bet*2
                    player_ar[2] = crafted_deck.pop()
                    valueP = func_values(player_ar)
                case 3:
                    valueP = func_values(player_ar)

            ui(Money, Score)
            if valueP > 21:
                Money -= bet
                func_printer(player_ar, 0)
                print("Value of the player Hand: ",valueP,"\n")
                print("You overpassed, you lost: $", bet)
            else:
                valueD = 0
                j = 0
                while valueD < 17:
                        dealer_ar[j+1] = crafted_deck.pop()
                        valueD = func_values(dealer_ar)
                        j += 1
                func_printer(dealer_ar, 1)
                print("Value of the dealer Hand: ",valueD,"\n")
                func_printer(player_ar, 0)
                print("Value of the player Hand: ",valueP,"\n")
                if valueP == 21:
                    print("\nBlackjack!\n")
                if valueD > 21:
                    Money += bet
                    print("Dealer overpassed, you won: $", bet*2)
                elif valueD > valueP:
                    Money -= bet
                    print("Dealer beat you with", valueD, "you lost: $", bet)
                elif valueD == valueP:
                    print("There is a Tie!")
                else:
                    Money += bet
                    print("You beat the dealer, you won: $", bet*2)
            cont()
        else:
            print("You have 21, you will win is there is no match on Blackjack")
            j = 0
            valueD = 0
            while valueD < 17:
                dealer_ar[j+1] = crafted_deck.pop()
                valueD = func_values(dealer_ar)
                j += 1
            func_printer(dealer_ar, 1)
            print("Value of the dealer Hand: ",valueD,"\n")
            func_printer(player_ar, 0)
            print("Value of the player Hand: ",valueP,"\n")
            if valueD != valueP:
                Money+=math.floor(bet*1.5)
                print("You won: $",math.floor(bet+bet*1.5)," big win")
            else:
                print("The dealer tied your Blackjack")
            cont()

    return Money

# Second and last to design ROULETTE!!
roulette_dict = { 0: "0",
    1: "■",  2: "▢",  3: "■",  4: "▢",  5: "■",  6: "▢", 7: "■",  8: "▢",  9: "■", 10: "▢", 11: "▢", 12: "■", 13: "▢", 14: "■", 15: "▢", 16: "■", 17: "▢", 18: "■",
    19: "■", 20: "▢", 21: "■", 22: "▢", 23: "■", 24: "▢", 25: "■", 26: "▢", 27: "■", 28: "▢", 29: "▢", 30: "■", 31: "▢", 32: "■", 33: "▢", 34: "■", 35: "▢", 36: "■" }

def roulette(Money,Score):
    while Money < Score and Money != 0:
        ui(Money, Score)
        bet = bet_val(Money)
        if bet == "NO":
            return Money
        while True:
            ui(Money,Score)
            type_bet = input("Select your number for the bet (only 1 choice).\n1 is for number.\n2 is for color.\n3 is for dozen.\n4 is for odd or even(excluding 0).\n5 is for 1-18 or 19-36.\nSelect your bet: ")
            if type_bet.isdigit() and 0 < int(type_bet) < 6:
                type= int(type_bet)
                roulette_slot = random.randint(0,36)
                char = roulette_dict[roulette_slot]
                match type:
                    case 1:
                        ui(Money,Score)
                        while True:
                            selector = input("Select your number: ")
                            if selector.isdigit() and -1 < int(selector) < 37:
                                break
                        print("\nRoulette stopped at: ",roulette_slot,char,"\n")
                        if int(selector) == roulette_slot:
                            Money+=bet*35
                            print(f"There is a match on {int(selector)} you won: $",bet*36,"\n")
                        else:
                            Money-=bet
                            print("No match you lose: $",bet,"\n")
                        cont()
                        break
                    case 2:
                        ui(Money,Score)
                        while True:
                            selector = input("Select your color.\n\n1 is for red.\n\n2 is for black.\n\nColor: ")
                            if selector.isdigit() and (int(selector) in (1,2)):
                                break
                        print("\nRoulette stoped at: ",roulette_slot,char,"\n")
                        if int(selector) == 1 and char == "■":
                            Money+=bet
                            print("There is a match on red you won: $",bet*2,"\n")
                        elif int(selector) == 2 and char == "▢":
                            Money+=bet
                            print("There is a match on black won: $",bet*2,"\n")
                        else:
                            Money-=bet
                            print("No match you lose: $",bet,"\n")
                        cont()
                        break
                    case 3:
                        ui(Money,Score)
                        while True:
                            selector = input("Select your Dozen.\n\n1 is for 1-12.\n\n2 is for 13-24.\n\n3 is for 25-36\n\nDozen: ")
                            if selector.isdigit() and (int(selector) in (1,2,3)):
                                break
                        print("\nRoulette stoped at: ",roulette_slot,char,"\n")
                        if int(selector) == 1 and 0 < roulette_slot < 13:
                            Money+=bet*2
                            print("There is a match in 1-12 you won: $",bet*3,"\n")
                        elif int(selector) == 2 and 12 < roulette_slot < 25:
                            Money+=bet*2
                            print("There is a match in 13-24 you won: $",bet*3,"\n")
                        elif int(selector) == 3 and 24 < roulette_slot < 37:
                            Money+=bet*2
                            print("There is a match in 25-36 you won: $",bet*3,"\n")
                        else:
                            Money-=bet
                            print("No match you lose: $",bet,"\n")
                        cont()
                        break
                    case 4:
                        ui(Money,Score)
                        while True:
                            selector = input("Select your parity.\n\n1 is for odd.\n\n2 is for even.\n\nParity: ")
                            if selector.isdigit() and (int(selector) in (1,2)):
                                break
                        print("\nRoulette stoped at: ",roulette_slot,char,"\n")
                        if int(selector) == 1 and roulette_slot%2 == 1:
                            Money+=bet
                            print("There is a match on odd you won: $",bet*2,"\n")
                        elif int(selector) == 2 and roulette_slot%2 == 0 and roulette_slot != 0:
                            Money+=bet
                            print("There is a match on even you won: $",bet*2,"\n")
                        else:
                            Money-=bet
                            print("No match you lose: $",bet,"\n")
                        cont()
                        break
                    case 5:
                        ui(Money,Score)
                        while True:
                            selector = input("Select your half.\n\n1 is for 1-18.\n\n2 is for 19-36.\n\nHalf: ")
                            if selector.isdigit() and (int(selector) in (1,2)):
                                break
                        print("\nRoulette stoped at: ",roulette_slot,char,"\n")
                        if int(selector) == 1 and 0 < roulette_slot < 19:
                            Money+=bet
                            print("There is a match on 1-18 you won: $",bet*2,"\n")
                        elif int(selector) == 2 and 18 < roulette_slot < 37:
                            Money+=bet
                            print("There is a match on 19-36 you won: $",bet*2,"\n")
                        else:
                            Money-=bet
                            print("No match you lose: $",bet,"\n")
                        cont()
                        break

    return Money

# Tercero en empezar a programar y el tercer juego ¿Quién lo diría?

# MULT FUNC for slots
def multiplier(rowf, mult):
    if rowf == "+":
        mult = 1
    elif rowf == "*":
        mult = 5
    elif rowf == "^":
        mult = 25
    else:
        mult = 200
    return mult

#Main for slots
def slotmachine(Money, Score):
    while Money < Score and Money != 0:
        ui(Money, Score)
        bet = bet_val(Money)
        if bet == "NO":
            return Money
        n = 3
        slots = [[""] * n for _ in range(n)]
        slot = ""
        bet = int(bet)
        Money -= bet
        for i in range(n):
            for j in range(n):
                randomizer = random.randint(1, 10000)
                if randomizer < 6001:
                    slot = "+"
                elif randomizer < 8501:
                    slot = "*"
                elif randomizer < 9501:
                    slot = "^"
                else:
                    slot = "$"
                slots[i][j] = slot

        wins = 0
        multi = 0

        # rows
        for row in slots:
            if all(symbol == row[0] for symbol in row):
                wins += 1
                multi += multiplier(row[0], multi)

        # 1diagonal
        diag1 = [slots[i][i] for i in range(n)]
        if all(symbol == diag1[0] for symbol in diag1):
            wins += 1
            multi += multiplier(diag1[0], multi)

        # 2diagonal
        diag2 = [slots[i][n - 1 - i] for i in range(n)]
        if all(symbol == diag2[0] for symbol in diag2):
            wins += 1
            multi += multiplier(diag2[0], multi)

        p = n
        print("")
        for p in slots:
            print(p)
            print("")

        if wins == 0:
            print("You lose $", bet, ":(")
        else:
            print("You won ", wins, "times! , for a total mult of ", multi, ".")
            Money += bet*multi
            print("You won $", (bet*multi), "Congratulations")
        cont()

    return Money

# Dados, basado en el juego de feria donde el 7 tenía un diablito
# Dictionary of mult
dic_mult = {2: 34, 12: 34, 3: 16, 11: 16, 4: 10, 10: 10, 5: 7, 9: 7, 6: 5, 8: 5, 7: 4}
# Function to win
def victory(Money, betN, matcher, mult):
    print("There's a match on ", matcher, " you won")
    Money += betN*mult
    print("You won $", betN*mult, ":)")
    return Money

def dices(Money, Score):
    while Money < Score and Money != 0:
        ui(Money, Score)
        bet = bet_val(Money)
        if bet == "NO":
            return Money
        while True:
            user_inp = input("Select your number: ")
            if user_inp.isdigit() and 1 < int(user_inp) < 13:
                user_num = int(user_inp)
                dice1 = random.randint(1, 6)
                dice2 = random.randint(1, 6)
                print("Your number: ", user_inp, "        Dice 1: ", dice1, "   Dice 2: ", dice2)
                print("Result:      ", (dice1+dice2))
                if user_num == (dice1+dice2):
                    mult = dic_mult[user_num]
                    Money = victory(Money, bet, user_num, mult)
                else:
                    print("There is no match, the house won")
                    print("You lose $", bet, ":(")
                    Money -= bet
                cont()
                break
    return Money

# Primero el juego más fácil // ¿Listo? 1.0
def coin(Money, Score):
    while Money < Score and Money != 0:
        ui(Money, Score)
        bet = bet_val(Money)
        if bet == "NO":
            return Money
        while True:
            risk = input("Choose 1 or 2 (1 is heads, 2 is tails) : ")
            if risk.isdigit() and (int(risk) in (1, 2)):
                election = int(risk)
                house_num = random.randint(1, 2)
                print("\nYour selection: ", election, "      Result: ", house_num)
                match house_num:
                    case 1:
                        if election == house_num:
                            print("\nThere's a match with heads you won\n")
                            Money += bet
                            print("You won $", bet, ":)\n")
                        else:
                            print("\nThe House beat you with heads\n")
                            Money -= bet
                            print("You lose $", bet, ":(\n")
                    case 2:
                        if election == house_num:
                            print("\nThere's a match with tails you won\n")
                            Money += bet
                            print("You won $", bet, ":)\n")
                        else:
                            print("\nThe House beat you with tails\n")
                            Money -= bet
                            print("You lose $", bet, ":(\n")
                cont()
                break
    return Money

# Print wellcome Message && Asking money
def Welcome():
    while True:
        Dbalance = input(
            "Welcome to Las Vegas, type your money (all the numbers typed must be positive integers and all must be in the provided range): ")
        if Dbalance.isdigit():
            Mbalance = int(Dbalance)
            if Mbalance > 0:
                return Mbalance

# Selecting Difficulty
def difficulty(Balance):
    while True:
        Dificulty = input(
            "Hello, in ALL IN you can only win until you have multiplied your money by: 64, 256 or 1024.\nType 1 for Easy Mode.\nType 2 for Medium Mode.\nType 3 for Hard Mode.\nDifficulty: ")
        if Dificulty.isdigit() and (int(Dificulty) in (1,2,3)):
            DSelector = int(Dificulty)
            match DSelector:
                case 1:
                    print("\nYou choose Easy Difficulty\n")
                    Score_to_beat = 64*Balance
                case 2:
                    print("\nYou choose Medium Difficulty\n")
                    Score_to_beat = 256*Balance
                case 3:
                    print("\nYou choose Hard Difficulty\n")
                    Score_to_beat = 1024*Balance
            cont()
            return Score_to_beat

# Game loop
def gameloop(Balance, Score):
    game_active = 1
    while game_active != 0:
        ui(Balance, Score)
        Game = input(
            "Now you are entering the game zone, type: 1 for BlackJack, 2 for Roulette, 3 for Slots, 4 for Dices, 5 for Coin: ")
        if Game.isdigit():
            gameN = int(Game)
            match gameN:
                case 1:
                    ui(Balance, Score)
                    print("Now you are entering the Blackjack zone, good luck :)\nRules:\nDealer Stops at 17 you may risk it until you have 21.\nIf you exceed 21 you lose.\nThe value of A is 11 unless it passes 21 (in that case is 1).\nThe value of K,Q and J is 10.\nThe other cards have the value indicated.\nHaving blackjack pays for 1.5 but since there's no cents in All In, the decimal numbers of the price will be removed (example 7.5 will become 7).\nYou choose the amount of decks between 5 and 8.\nNo insurance.\n1 hand at the time (no split).\n")
                    cont()
                    Balance = blackjack(Balance, Score)
                    game_active = print_state(Balance,Score)
                case 2:
                    print("Now you are entering the Roulette zone, good luck :)\nRules:\nThis is an european roulette you can bet in any number from 0 to 36, on any color between red and black, on any Dozen, on odd number or even, and 1-18 or 19-36")
                    cont()
                    Balance = roulette(Balance,Score)
                    game_active = print_state(Balance,Score)
                case 3:
                    ui(Balance, Score)
                    print("Now you are entering the Slot Machine zone, good luck :)\n\nYou win if 3 symbols match horizontally or via the diagonal that passes the middle (5 chances in total).\nYou can win multiple times.\n+++: pays the bet\n***: pays 5 times the bet\n^^^: pays 25 times the bet\n$$$: pays 200 times the bet.\n")
                    cont()
                    Balance = slotmachine(Balance, Score)
                    game_active = print_state(Balance,Score)
                case 4:
                    ui(Balance, Score)
                    print("Now you are entering the Dices zone, good luck :)\nRules:\nHouse will roll 2 dice, you may select a number between 2 an 12, numbers pay more according to the chances.\n2 and 12 pay 34 times the bet.\n3 and 11 pay 16 times the bet.\n4 and 10 pay 10 times the bet.\n5 and 9 pay 7 times the bet.\n6 and 8 pay 5 times the bet\n7 pay 4 times the bet.\n")
                    cont()
                    Balance = dices(Balance, Score)
                    game_active = print_state(Balance,Score)
                case 5:
                    ui(Balance, Score)
                    print("Now you are entering the Coin zone , good luck :)\nRules:\nA match is a win, different faces mean you lose.")
                    cont()
                    Balance = coin(Balance, Score)
                    game_active = print_state(Balance,Score)
                case _:
                    continue

# Execution
def main():
    Balance = Welcome()
    beat_score = difficulty(Balance)
    Balance = gameloop(Balance, beat_score)

# Run execution
main()

