# Casino vegas

# Nota personal, implementar UI con dinero a conseguir y balance actual
# Nota personal, implementar hacer el type de "rules" para mostrar las reglas
# Nota personal, se puede hacer módulo de la validación inicial pero con ¿Rules?
import random
import os

# Function clear screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Function to continue
def cont():
    while True:
        cont = input("Press ENTER to continue: ")
        if cont == "":
            break

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

# Main to Blackjack
def blackjack(Money, Score):
    while True:
        decks_in = input(
            "\nSelect the amount of decks you are going to play with (an int between 5 and 8): ")
        if decks_in.isdigit() and 4 < int(decks_in) < 9:
            decks = int(decks_in)
            break
    while True:
        def build_deck(n_decks):
            suits = ["♠", "♥", "♦", "♣"]
            value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
            baraja = [f"{v}{p}" for p in suits for v in value]
            total_deck = baraja * n_decks
            random.shuffle(total_deck)
            return total_deck
        crafted_deck = build_deck(decks)
        initial_size = len(crafted_deck)
        ui(Money, Score)
        bet = input(
            "Select the ammount of the bet (no limits, and put a valid ammount) or type NO to leave: ")
        if bet == "NO":
            return Money
        while True:
            # Re Shuffle if needed
            if len(crafted_deck) < (initial_size/4):
                print("Casino is running out of cards, we need to reshuffle")
                crafted_deck = build_deck(decks)
            if bet.isdigit() and (int(bet) > 0) and (int(bet) <= Money):
                betN = int(bet)
                dealer_ar = [""] * 16
                player_ar = [""] * 20
                # Carta dealer
                dealer_ar[0] = crafted_deck.pop()
                # Función imprimir
                print("")
                func_printer(dealer_ar, 1)
                print("")
                # Primera carta jugador
                player_ar[0] = crafted_deck.pop()
                # Segunda carta jugador
                player_ar[1] = crafted_deck.pop()
                # función imprimir
                func_printer(player_ar, 0)
                valueP = func_values(player_ar)
                if valueP != 21:
                    print("\n1 for hit.\n2 for double.\n3 for stay.\n")
                while True:
                    if valueP == 21:
                        break
                    election = input("Hit, double or stay: ")
                    if election.isdigit() and (int(election) in (1, 2, 3)):
                        action = int(election)
                        match action:
                            case 1:
                                i = 0
                                while action != 3:
                                    print("\n1 for hit.\n3 for stay.\n")
                                    player_ar[i+2] = crafted_deck.pop()
                                    valueP = func_values(player_ar)
                                    print("")
                                    func_printer(dealer_ar, 1)
                                    print("")
                                    func_printer(player_ar, 0)
                                    print("")
                                    i += 1
                                    if valueP >= 21:
                                        break
                                    else:
                                        while True:
                                            election = input("Hit or stay: ")
                                            if election.isdigit() and (int(election) in (1, 3)):
                                                action = int(election)
                                                break
                                break

                            case 2:
                                betN = betN*2
                                player_ar[2] = crafted_deck.pop()
                                break
                            case 3:
                                valueP = func_values(player_ar)
                                break
                if valueP > 21:
                    print("")
                    func_printer(dealer_ar, 1)
                    print("")
                    func_printer(player_ar, 0)
                    print("")
                    Money -= betN
                    print("You overpassed, you lost: $", betN)
                    if Money == 0:
                        return Money
                    cont()
                    break
                else:
                    j = 0
                    valueD = 0
                    while valueD < 17:
                        dealer_ar[j+1] = crafted_deck.pop()
                        valueD = func_values(dealer_ar)
                        j += 1
                    print("")
                    func_printer(dealer_ar, 1)
                    print("")
                    func_printer(player_ar, 0)
                    print("")
                    if valueP == 21:
                        print("\nBlackjack!\n")
                    if valueD > 21:
                        Money += betN
                        print("Dealer overpassed, you won: $", betN)
                        if Money >= Score:
                            return Money
                        cont()
                        break
                    elif valueD > valueP:
                        Money -= betN
                        print("Dealer beated you with", valueD, "you lost: $", betN)
                        if Money == 0:
                            return Money
                        cont()
                        break
                    elif valueD == valueP:
                        print("There is a Tie!")
                        cont()
                        break
                    else:
                        Money += betN
                        print("You beated the dealer, you won: $", betN)
                        if Money >= Score:
                            return Money
                        cont()
                        break

            else:
                break

# Second and last to design ROULETTE!!
roulette_dict = {
    0: "▣",
    1: "▢", 2: "■", 3: "▢", 4: "■", 5: "▢", 6: "■",
    7: "▢", 8: "■", 9: "▢", 10: "■", 11: "■", 12: "▢",
    13: "■", 14: "▢", 15: "■", 16: "▢", 17: "■", 18: "▢",
    19: "▢", 20: "■", 21: "▢", 22: "■", 23: "▢", 24: "■",
    25: "▢", 26: "■", 27: "▢", 28: "■", 29: "■", 30: "▢",
    31: "■", 32: "▢", 33: "■", 34: "▢", 35: "■", 36: "▢"
}

def roulette(Money,Score):
    while True:
        ui(Money, Score)
        bet = input(
            "Select the ammount of the bet (no limits, and put a valid ammount) or type NO to leave: ")
        if bet == "NO":
            return Money
        while True:
            if bet.isdigit() and (int(bet) > 0) and (int(bet) <= Money):
                type_bet = input("Select your number for the bet (only 1 choice).\n1 is for number.\n2 is for color\n3 is for docen\n4 is for odd or even(excluding 0)\n5 is for 1-18 or 19-36\nSelect your bet: ")
                if type_bet.isdigit() and 1 < int(type_bet) < 13:
                    type= int(type_bet)
                    roulette_slot = random.randint(0,36)
                    char = roulette_dict[roulette_slot]
                    match type:
                        case 1:
                            while True:
                                selector = input("Select your number: ")
                                if selector.isdigit() and -1 < int(selector) < 37:
                                    break
                            break
                        case 2:
                            while True:
                                selector = input("Select your color.\n\n1 is for red.\n\n2 is for black.\n\nColor: ")
                                if selector.isdigit() and (int(selector) in (1,2)):
                                    break
                            break
                        case 3:
                            while True:
                                selector = input("Select your docen.\n\n1 is for 1-12.\n\n2 is for 13-24.\n\n3 is for 25-36\n\nColor: ")
                                if selector.isdigit() and (int(selector) in (1,2)):
                                    break
                            break
                        case 4:
                            while True:
                                selector = input("Select your parity.\n\n1 is for odd.\n\n2 is for even.\n\nParity: ")
                                if selector.isdigit() and (int(selector) in (1,2)):
                                    break
                            break
                        case 5:
                            while True:
                                selector = input("Select your half.\n\n1 is for 1-18.\n\n2 is for 19-36.\n\nParity: ")
                                if selector.isdigit() and (int(selector) in (1,2)):
                                    break
                            break

# Tercero en empezar a programar y el tercer juego ¿Quién lo diría?
def slotmachine(Money, Score):
    while True:
        ui(Money, Score)
        bet = input(
            "Select the ammount of the bet (no limits, and put a valid ammount) or type NO to leave: ")
        if bet == "NO":
            return Money
        while True:
            if bet.isdigit() and (int(bet) > 0) and (int(bet) <= Money):
                n = 3
                slots = [[""] * n for _ in range(n)]
                slot = ""
                betN = int(bet)
                Money -= betN
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

                # MULT FUNC
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
                    print("You lose $", betN, ":(")
                    if Money == 0:
                        return Money
                    cont()
                    break
                else:
                    print("You won ", wins, "times! , for a total mult of ", multi, ".")
                    Money += betN*multi
                    print("You won $", (betN*multi), "Cogratulations")
                    cont()
                    if Money >= Score:
                        return Money
                    break
            else:
                break

# Dados, basado en el juego de feria donde el 7 tenía un diablito
def victory(Money, betN, matcher, mult):
    print("There's a match on ", matcher, " you won")
    Money += betN*mult
    print("You won $", betN*mult, ":)")
    return Money

def dices(Money, Score):
    while True:
        ui(Money, Score)
        bet = input(
            "Select the ammount of the bet (no limits, and put a valid ammount) or type NO to leave: ")
        if bet == "NO":
            return Money
        while True:
            if bet.isdigit() and (int(bet) > 0) and (int(bet) <= Money):
                betN = int(bet)
                user_inp = input("Select your number: ")
                if user_inp.isdigit() and 1 < int(user_inp) < 13:
                    user_num = int(user_inp)
                    dice1 = random.randint(1, 6)
                    dice2 = random.randint(1, 6)
                    print("Your number: ", user_inp, "        Dice 1: ", dice1, "   Dice 2: ", dice2)
                    print("Result:      ", (dice1+dice2))
                    if user_num == (dice1+dice2):
                        match user_num:
                            case 2:
                                mult = 34
                                Money = victory(Money, betN, user_num, mult)
                                cont()
                            case 3:
                                mult = 16
                                Money = victory(Money, betN, user_num, mult)
                                cont()
                            case 4:
                                mult = 10
                                Money = victory(Money, betN, user_num, mult)
                                cont()
                            case 5:
                                mult = 7
                                Money = victory(Money, betN, user_num, mult)
                                cont()
                            case 6:
                                mult = 5
                                Money = victory(Money, betN, user_num, mult)
                                cont()
                            case 7:
                                mult = 4
                                Money = victory(Money, betN, user_num, mult)
                                cont()
                            case 8:
                                mult = 5
                                Money = victory(Money, betN, user_num, mult)
                                cont()
                            case 9:
                                mult = 7
                                Money = victory(Money, betN, user_num, mult)
                                cont()
                            case 10:
                                mult = 10
                                Money = victory(Money, betN, user_num, mult)
                                cont()
                            case 11:
                                mult = 16
                                Money = victory(Money, betN, user_num, mult)
                                cont()
                            case 12:
                                mult = 34
                                Money = victory(Money, betN, user_num, mult)
                                cont()
                        if Money >= Score:
                            return Money
                        break
                    else:
                        print("There is no match, the house won")
                        print("You lose $", betN, ":(")
                        Money -= betN
                        if Money == 0:
                            return Money
                        cont()
                        break
            else:
                break

# Primero el juego más fácil // ¿Listo? 1.0
def coin(Money, Score):
    while True:
        ui(Money, Score)
        bet = input(
            "Select the ammount of the bet (no limits, and put a valid ammount) or type NO to leave: ")
        if bet == "NO":
            return Money
        while True:
            if bet.isdigit() and (int(bet) > 0) and (int(bet) <= Money):
                betN = int(bet)
                risk = input("Choose 1 or 2 (1 is heads, 2 is tails) : ")
                if risk.isdigit() and (int(risk) in (1, 2)):
                    election = int(risk)
                    house_num = random.randint(1, 2)
                    print("\nYour selection: ", election, "      Result: ", house_num)
                    match house_num:
                        case 1:
                            if election == house_num:
                                print("\nTheres a match with heads you won\n")
                                Money += betN
                                print("You won $", betN, ":)\n")
                                cont()
                                if Money >= Score:
                                    return Money
                            else:
                                print("\nThe House beated you with heads\n")
                                Money -= betN
                                print("You lose $", betN, ":(\n")
                                if Money == 0:
                                    return Money
                                cont()
                            break
                        case 2:
                            if election == house_num:
                                print("\nTheres a match with tails you won\n")
                                Money += betN
                                print("You won $", betN, ":)\n")
                                cont()
                                if Money >= Score:
                                    return Money
                            else:
                                print("\nThe House beated you with tails\n")
                                Money -= betN
                                print("You lose $", betN, ":(\n")
                                if Money == 0:
                                    return Money
                                cont()
                            break
            else:
                break


def wellcome():
    while True:
        Dbalance = input(
            "Wellcome to Las Vegas, type your money (all the numbers typed must be possitive integers and all must be in the provided range): ")
        if Dbalance.isdigit():
            Mbalance = int(Dbalance)
            if Mbalance > 0:
                return Mbalance


def difficulty(Balance):
    while True:
        Dificulty = input(
            "Hello, in ALL IN you can only win until you have multiplied your money by: 64, 256 or 1024.\nType 1 for Easy Mode.\nType 2 for Medium Mode.\nType 3 for Hard Mode.\nDifficulty: ")
        if Dificulty.isdigit():
            DSelector = int(Dificulty)
            match DSelector:
                case 1:
                    print("\nYou  choose Easy Difficulty\n")
                    Score_to_beat = 64*Balance
                    cont()
                    return Score_to_beat
                case 2:
                    print("\nYou  choose Medium\n")
                    Score_to_beat = 256*Balance
                    cont()
                    return Score_to_beat
                case 3:
                    print("\nYou  choose Hard\n")
                    Score_to_beat = 1024*Balance
                    cont()
                    return Score_to_beat
                case _:
                    continue


def gameloop(Balance, Score):
    while True:
        ui(Balance, Score)
        Game = input(
            "Now you are entering the game zone, type: 1 for BlackJack, 2 for Roulette, 3 for Slots, 4 for Dices, 5 for Coin: ")
        if Game.isdigit():
            gameN = int(Game)
            match gameN:
                case 1:
                    ui(Balance, Score)
                    print("Now you are entering the Blackjack zone, good luck :)")
                    print("Rules:\nDealer Stops at 17 you may risk it until you have 21. ")
                    cont()
                    Balance = blackjack(Balance, Score)
                    if Balance == 0:
                        print("You are broke now, go back to home")
                        break
                    elif Balance >= Score:
                        print("You win, the casino is broke now :(")
                        break
                    print("You managed to get out with: $", Balance)
                case 2:
                    print("Now you are entering the Roulette zone, good luck :)\nRules:\nThis is an european roulette you can bet in any number from 0 to 36, on any color between red and black, on any docen, on odd number or even, and 1-18 or 19-36")
                    cont()
                    Balance = roulette(Balance,Score)
                case 3:
                    ui(Balance, Score)
                    print("Now you are entering the Slot Machine zone, good luck :)\n\nYou win if 3 symbols match horizontally or via the diagonal that passes the middle (5 chances in total).\nYou can win multiple times.\n+++: pays the bet\n***: pays 5 times the bet\n^^^: pays 25 times the bet\n$$$: pays 200 times the bet.\n")
                    cont()
                    Balance = slotmachine(Balance, Score)
                    if Balance == 0:
                        print("You are broke now, go back to home")
                        break
                    elif Balance >= Score:
                        print("You win, the casino is broke now :(")
                        break
                    print("You managed to get out with: $", Balance)
                case 4:
                    ui(Balance, Score)
                    print("Now you are entering the Dices zone, good luck :)")
                    print("Rules:\nHouse will roll 2 dices, you may select a number between 2 an 12, numbers pay more according to the chances.\n2 and 12 pay 34 times the bet.\n3 and 11 pay 16 times the bet.\n4 and 10 pay 10 times the bet.\n5 and 9 pay 7 times the bet.\n6 and 8 pay 5 times the bet\n7 pay 4 times the bet.\n")
                    cont()
                    Balance = dices(Balance, Score)
                    if Balance == 0:
                        print("You are broke now, go back to home")
                        break
                    elif Balance >= Score:
                        print("You win, the casino is broke now :(")
                        break
                    print("You managed to get out with: $", Balance)
                case 5:
                    ui(Balance, Score)
                    print("Now you are entering the Coin zone , good luck :)")
                    print("Rules:\nA match is a win, diferent faces you loose.")
                    cont()
                    Balance = coin(Balance, Score)
                    if Balance == 0:
                        print("You are broke now, go back to home")
                        break
                    elif Balance > Score:
                        print("You win, the casino is broke now :(")
                        break
                    print("You managed to get out with: $", Balance)
                case _:
                    continue


def main():
    Balance = wellcome()
    beat_score = difficulty(Balance)
    Balance = gameloop(Balance, beat_score)

main()

