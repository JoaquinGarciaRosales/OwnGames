import chess
import random

VALOR_PIEZAS = {
  chess.PAWN: 1,
  chess.KNIGHT: 3,
  chess.BISHOP: 3,
  chess.ROOK: 5,
  chess.QUEEN: 9,
  chess.KING: 0,
}

def movimiento_bot(board):
  movimientos_posibles = list(board.legal_moves)
  
  best_score = float("-inf")
  mejores = []
  
  for m in movimientos_posibles:
    score = (
    (0.35  * develop_score(board, m)) +
    (0.65  * scape_score(board, m)) +
    (1.3  * capture_score(board, m)) +
    (0.25 * attack_score(board, m)) +
    (1.1 * hanging_penalty(board, m)) +
    (0.4  * king_safety_score(board, m)) +   
    (0.85  * check_score(board, m))          
    )
    
    if score > best_score:
      best_score = score
      mejores = [m]
    elif score == best_score:
      mejores.append(m)
  
  return random.choice(mejores)

#El lugar de destino del movimiento actual se considera "Seguro" auxiliar
def is_safe(board,move):
  
  board.push(move)
  
  casilla = move.to_square
  atacado = board.is_attacked_by(board.turn, casilla)
  
  board.pop()
  
  return not atacado
  
#heurística de evaluación de capturas
def capture_score(board,move):
  if not board.is_capture(move):
    return 0
  
  pieza = board.piece_at(move.from_square)
  capturada = board.piece_at(move.to_square)
  
  if pieza is None or capturada is None:
    return 0
  
  valor_propio = VALOR_PIEZAS[pieza.piece_type]
  valor_objetivo = VALOR_PIEZAS[capturada.piece_type]
  
  if is_safe(board,move):
    return valor_objetivo
  
  return valor_objetivo - valor_propio
  
#Heurística desarrollar piezas menores
def develop_score(board,move):
  pieza = board.piece_at(move.from_square)
  
  if pieza is None:
    return 0
  
  score = 0
  
  #en teoría es bueno buscar actividad de piezas menores pero este de aquí produce resultados extraños
  #if pieza.piece_type in [chess.KNIGHT, chess.BISHOP]:
   # score += 1
  if pieza.piece_type == chess.PAWN:
    if move.from_square in [chess.D7, chess.E7]:
      if move.to_square in [chess.D5, chess.E5]:
        score +=.92
      else:
        score +=.71
    if move.from_square in [chess.B7, chess.G7]:
      score +=.32
    
  if pieza.piece_type in [chess.KNIGHT, chess.BISHOP]:  
    if move.from_square in [chess.B8, chess.G8, chess.C8, chess.F8]:
      score +=.45
  
  return score

#auxiliar para huerísticas
def is_in_danger(board, casilla):
  return board.is_attacked_by(chess.WHITE, casilla)

#heuristica de escape
def scape_score(board, move):
  pieza = board.piece_at(move.from_square)
  
  if pieza is None:
    return 0
  
  valor = VALOR_PIEZAS[pieza.piece_type]
  
  if not is_in_danger(board,move.from_square):
    return 0
  
  if is_safe (board,move):
    return valor
  
  return 0

#heurística ataque
def attack_score(board, move):
  board.push(move)
  
  score = 0
  
  for square in chess.SQUARES:
    pieza = board.piece_at(square)
    
    if pieza and pieza.color == chess.WHITE:
      if board.is_attacked_by(chess.BLACK, square):
        valor = VALOR_PIEZAS[pieza.piece_type]
        
        defensores = board.attackers(chess.WHITE, square)
        
        if not defensores:
          score += 0.4 * valor
        else:
          score += 0.15* valor
  
  board.pop()
  
  return score
          
#Heurística de penalización de piezas colgadas
def hanging_penalty(board, move):
  board.push(move)
  penalizacion = 0

  for square in chess.SQUARES:
      pieza = board.piece_at(square)
      if pieza and pieza.color == chess.BLACK:
          atacantes = board.attackers(chess.WHITE, square)
          if atacantes:
              defensores = board.attackers(chess.BLACK, square)
              if not defensores:
                  penalizacion -= VALOR_PIEZAS[pieza.piece_type]
              else:
                  penalizacion -= 0.5 * VALOR_PIEZAS[pieza.piece_type]

  board.pop()
  return penalizacion

  
#heurística buscar jaques y premiar el mate
def check_score(board, move):
  board.push(move)
  if board.is_checkmate() and board.turn == chess.WHITE:
    board.pop()
    return 10000
  score = 0
  
  if board.is_check():
    score += 2.0
    rey_blanco = board.king(chess.WHITE)
    if rey_blanco is not None:
      if chess.square_rank(rey_blanco) in (0, 7) or chess.square_file(rey_blanco) in (0, 7):
        score += 2.0
      
      escapes = 0
      for sq in chess.SQUARES:
        if chess.square_distance(rey_blanco, sq) == 1:
          if not board.is_attacked_by(chess.BLACK, sq) and board.piece_at(sq) is None:
            escapes += 1
      
      score += (3 - escapes) * 0.5
      
      if escapes == 0 and not board.is_checkmate():
        score -= 2.0
  board.pop()
  return score

#heurística proteger el rey
def king_safety_score(board, move):
  board.push(move)
  
  #Bool para verificar mate inminente
  mate_amenaza = False
  if board.turn == chess.WHITE:
    for respuesta in board.legal_moves:
      board.push(respuesta)
      if board.is_checkmate():
        mate_amenaza = True
        board.pop()
        break
      board.pop()
  
  if mate_amenaza:
    board.pop()
    return -10000 
  
  def contar_amenazas_al_rey(tablero):
    rey_sq = tablero.king(chess.BLACK)
    if rey_sq is None:
      return 0
    amenazas = 0
    for sq in chess.SQUARES:
      if chess.square_distance(rey_sq, sq) <= 2:
        if tablero.is_attacked_by(chess.WHITE, sq):
          amenazas += 1
    return amenazas

  def bonus_enroque(tablero):
    rey_sq = tablero.king(chess.BLACK)
    if rey_sq is None:
      return 0
    if rey_sq == chess.G8:
      if (tablero.piece_at(chess.F8) == chess.Piece(chess.ROOK, chess.BLACK) or
          tablero.piece_at(chess.H8) == chess.Piece(chess.ROOK, chess.BLACK)):
        return 1.5
    elif rey_sq == chess.C8:
      if (tablero.piece_at(chess.D8) == chess.Piece(chess.ROOK, chess.BLACK) or
          tablero.piece_at(chess.A8) == chess.Piece(chess.ROOK, chess.BLACK)):
        return 1.5
    return 0

  amenazas_actual = contar_amenazas_al_rey(board)
  bonus_actual = bonus_enroque(board)
  
  board.pop()
  return -0.5 * amenazas_actual + bonus_actual

