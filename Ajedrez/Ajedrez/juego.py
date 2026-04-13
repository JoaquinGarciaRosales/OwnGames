import chess
from bot import movimiento_bot

board = chess.Board()

print("----------------")
print(board.unicode())
print("----------------")
    
while not board.is_game_over():

    if board.turn:
        move_input = input("Turno humano (ej: e2e4): ")
        
        try:
            move = chess.Move.from_uci(move_input)
            if move in board.legal_moves:
                board.push(move)
                print("----------------")
                print(board.unicode())
                print("----------------")
                print("Turno máquina ")
            else:
                print("Movimiento ilegal")
        except:
            print("Formato inválido")
    else:
        #move = random.choice(list(board.legal_moves))
        move = movimiento_bot(board)
        board.push(move)
        print("----------------")
        print(board.unicode())
        print("----------------")

print("----------------")
print(board.unicode())
print("----------------")