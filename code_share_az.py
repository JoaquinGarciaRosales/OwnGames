# Casino vegas

#Nota personal, implementar UI con dinero a conseguir y balance actual
#Nota personal, implementar hacer el type de "rules" para mostrar las reglas
#Nota personal, se puede hacer módulo de la validación inicial pero con ¿Rules?
import random
import os

#Function clear screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")
# Function to continue
def cont():
    while True:
        cont = input("Press ENTER to continue: ")
        if cont == "":
            break
# Game UI
def ui(money,score):
    clear()
    while True:
        print(" __________________________________________________________________________________________________________")
        print("|Current Balance: $",money, "     You need to get: ",(score-money), "more      ", "Score needed: $",score,)
        print("|__________________________________________________________________________________________________________")
        break
# El más complicado
def blackjack(Money, Score):
    while True:
        ui(Money,Score)
        bet= input("Select the ammount of the bet (no limits, and put a valid ammount) or type NO to leave:  : ")
        if bet == "NO":
            return Money
        while True:
            if bet.isdigit() and (int(bet) > 0) and (int(bet)<=Money):
                betN = int(bet)
                #Función cartas
                def card():
                    card = random.randint(1,13)
                    if card in(1,11,12,13):
                        match card:
                            case 1:
                                card_char = "A"
                            case 11:
                                card_char = "J"
                            case 12:
                                card_char = "Q"
                            case 13:
                                card_char = "K"
                    else:
                        card_char = card
                    return card_char

                #Carta dealer
                carta1D = card()
                print ("Dealer card ", carta1D)
                #Primera carta jugador
                carta1J= card()
                #Segunda carta jugador
                carta2J= card()
                print("Player Cards: ", carta1J, carta2J)
                input("Hit, stay or doble")
            else:
                break

# Tercero en empezar a programar y el tercer juego ¿Quién lo diría?
def slotmachine(Money, Score):
    while True:
        ui(Money, Score)
        bet = input("Select the ammount of the bet (no limits, and put a valid ammount) or type NO to leave: ")
        if bet == "NO":
            return Money
        while True:
            if bet.isdigit() and (int(bet) > 0) and (int(bet)<=Money):
                n = 3
                slots = [[""] * n for _ in range(n)]
                slot = ""
                betN = int(bet)
                Money -= betN
                for i in range(n):
                    for j in range(n):
                        randomizer = random.randint(1,10000)
                        if randomizer < 6001:
                            slot = "+"
                        elif randomizer < 8501:
                            slot = "*"
                        elif randomizer < 9501:
                            slot = "^"
                        else:
                            slot = "$"
                        slots[i][j] = slot
                #MULT FUNC
                def multiplier(rowf,mult):
                    if rowf=="+":
                        mult = 1
                    elif rowf=="*":
                        mult = 5
                    elif rowf=="^":
                        mult = 25
                    else:
                        mult = 200
                    return mult

                wins = 0
                multi = 0

                #rows
                for row in slots:
                    if all(symbol == row[0] for symbol in row):
                        wins += 1
                        multi += multiplier(row[0],multi)

                #1diagonal
                diag1 = [slots[i][i] for i in range(n) ]
                if all(symbol == diag1[0] for symbol in diag1):
                    wins += 1
                    multi += multiplier(diag1[0],multi)

                #2diagonal
                diag2 = [slots[i][n - 1 - i] for i in range(n) ]
                if all(symbol == diag2[0] for symbol in diag2):
                    wins += 1
                    multi += multiplier(diag2[0],multi)

                p=n
                for p in slots:
                    print(p)
                    print("")

                if wins == 0:
                    print("You lose $",betN, ":(")
                    if Money == 0:
                        return Money
                    cont()
                    break
                else:
                    print("You won ",wins, "times! , for a total mult of ",multi,".")
                    Money += betN*multi
                    print("You won $",(betN*multi),"Cogratulations")
                    cont()
                    if Money >= Score:
                        return Money
                    break
            else:
                break
# Dados, basado en el juego de feria donde el 7 tenía un diablito
def victory(Money,betN,matcher,mult):
    print("There's a match on ",matcher," you won")
    Money += betN*mult
    print("You won $",betN*mult, ":)")
    return Money

def dices(Money,Score):
    while True:
        ui(Money, Score)
        bet= input("Select the ammount of the bet (no limits, and put a valid ammount) or type NO to leave: ")
        if bet == "NO":
            return Money
        while True:
            if bet.isdigit() and (int(bet) > 0) and (int(bet)<=Money):
                betN = int(bet)
                user_inp = input("Select your number: ")
                if user_inp.isdigit() and 1 < int(user_inp) < 13:
                    user_num= int(user_inp)
                    dice1 = random.randint(1,6)
                    dice2 = random.randint(1,6)
                    print("Your number: ",user_inp,"        Dice 1: ",dice1,"   Dice 2: ",dice2)
                    print("Result:      ",(dice1+dice2))
                    if user_num == (dice1+dice2):
                        match user_num:
                            case 2:
                                mult=34
                                Money=victory(Money,betN,user_num,mult)
                                cont()
                            case 3:
                                mult=16
                                Money=victory(Money,betN,user_num,mult)
                                cont()
                            case 4:
                                mult=10
                                Money=victory(Money,betN,user_num,mult)
                                cont()
                            case 5:
                                mult=7
                                Money=victory(Money,betN,user_num,mult)
                                cont()
                            case 6:
                                mult=5
                                Money=victory(Money,betN,user_num,mult)
                                cont()
                            case 7:
                                mult=4
                                Money=victory(Money,betN,user_num,mult)
                                cont()
                            case 8:
                                mult=5
                                Money=victory(Money,betN,user_num,mult)
                                cont()
                            case 9:
                                mult=7
                                Money=victory(Money,betN,user_num,mult)
                                cont()
                            case 10:
                                mult=10
                                Money=victory(Money,betN,user_num,mult)
                                cont()
                            case 11:
                                mult=16
                                Money=victory(Money,betN,user_num,mult)
                                cont()
                            case 12:
                                mult=34
                                Money=victory(Money,betN,user_num,mult)
                                cont()
                        if Money >= Score:
                            return Money
                        break
                    else:
                        print("There is no match, the house won")
                        print("You lose $",betN, ":(")
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
        bet= input("Select the ammount of the bet (no limits, and put a valid ammount) or type NO to leave: ")
        if bet == "NO":
            return Money
        while True:
            if bet.isdigit() and (int(bet) > 0) and (int(bet)<=Money):
                betN = int(bet)
                risk = input("Choose 1 or 2 (1 is heads, 2 is tails) : ")
                if risk.isdigit() and (int(risk) in (1,2)):
                    election = int(risk)
                    house_num = random.randint(1,2)
                    print("Your selection: ",election,"      Result: ",house_num)
                    match house_num:
                        case 1:
                            if election == house_num:
                                print("Theres a match with heads you won")
                                Money += betN
                                print("You won $",betN, ":)")
                                cont()
                                if Money >= Score:
                                    return Money
                            else:
                                print("The House beated you with heads")
                                Money -= betN
                                print("You lose $",betN, ":(")
                                if Money == 0:
                                    return Money
                                cont()
                            break
                        case 2:
                            if election == house_num:
                                print("Theres a match with tails you won")
                                Money += betN
                                print("You won $",betN, ":)")
                                cont()
                                if Money >= Score:
                                    return Money
                            else:
                                print("The House beated you with tails")
                                Money -= betN
                                print("You lose $",betN, ":(")
                                if Money == 0:
                                    return Money
                                cont()
                            break
            else:
                break

def wellcome():
    while True:
        Dbalance = input("Wellcome to Las Vegas, type your money (all the numbers typed must be possitive integers and all must be in the provided range): ")
        if Dbalance.isdigit():
            Mbalance= int(Dbalance)
            if Mbalance > 0:
                return Mbalance

def difficulty(Balance):
    while True:
        Dificulty = input("Hello, in ALL IN you can only win until you have multiplied your money by: 64, 256 or 1024. Type 1 for Easy Mode. Type 2 for Medium Mode. Type 3 for Hard Mode: ")
        if Dificulty.isdigit():
                DSelector= int(Dificulty)
                match DSelector:
                    case 1:
                        print("You  choose Easy Difficulty")
                        Score_to_beat=64*Balance
                        cont()
                        return Score_to_beat
                    case 2:
                        print("You  choose Medium")
                        Score_to_beat=256*Balance
                        cont()
                        return Score_to_beat
                    case 3:
                        print("You  choose Hard")
                        Score_to_beat=1024*Balance
                        cont()
                        return Score_to_beat
                    case _:
                        continue

def gameloop(Balance, Score):
    while True:
        ui(Balance, Score)
        Game = input("Now you are entering the game zone, type: 1 for BlackJack, 2 for Roulette, 3 for Slots, 4 for Dices, 5 for Coin: ")
        if Game.isdigit():
            gameN = int(Game)
            match gameN:
                case 1:
                    ui(Balance, Score)
                    print("Now you are entering the Blackjack zone, good luck :)")
                    print("Rules: Dealer Stops at 17 you may risk it until you have 21. ")
                    cont()
                    Balance = blackjack(Balance, Score)
                    if Balance == 0:
                        print("You are broke now, go back to home")
                        break
                    elif Balance >= Score:
                        print("You win, the casino is broke now :(")
                        break
                    print("You managed to get out with: $",Balance)
                case 2:
                    print("Now you are entering the Roulette zone, good luck :)")
                case 3:
                    ui(Balance, Score)
                    print("Now you are entering the Slot Machine zone, good luck :)")
                    print("Rules: +++: pays the bet // ***: pays 5 times the bet // ^^^: pays 25 times the bet // $$$: pays 200 times the bet. You win if 3 symbols match horizontally or via the diagonal that passes the middle (5 chances in total). You can win multiple times.")
                    cont()
                    Balance = slotmachine(Balance, Score)
                    if Balance == 0:
                        print("You are broke now, go back to home")
                        break
                    elif Balance >= Score:
                        print("You win, the casino is broke now :(")
                        break
                    print("You managed to get out with: $",Balance)
                case 4:
                    ui(Balance, Score)
                    print("Now you are entering the Dices zone, good luck :)")
                    print("House will roll 2 dices, you may select a number between 2 an 12, numbers pay more according to their chances ")
                    cont()
                    Balance = dices(Balance, Score)
                    if Balance == 0:
                        print("You are broke now, go back to home")
                        break
                    elif Balance >= Score:
                        print("You win, the casino is broke now :(")
                        break
                    print("You managed to get out with: $",Balance)
                case 5:
                    ui(Balance, Score)
                    print("Now you are entering the Coin zone , good luck :)")
                    print("Rules: A match is a win, diferent faces you loose.")
                    cont()
                    Balance = coin(Balance, Score)
                    if Balance == 0:
                        print("You are broke now, go back to home")
                        break
                    elif Balance > Score:
                        print("You win, the casino is broke now :(")
                        break
                    print("You managed to get out with: $",Balance)
                case _:
                    continue

def main():
    Balance = wellcome()
    beat_score = difficulty(Balance)
    Balance = gameloop(Balance,beat_score)
main()

