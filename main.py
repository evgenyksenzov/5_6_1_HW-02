def getInput(prompt, cast=None, condition=None, errorMessage=None):
  while True:
      try:
          val = cast(input(prompt))
          assert condition is None or condition(val)
          return val
      except:
          print(errorMessage or "Неверный ввод")

def printBoard(board):
  print()
  for row in board:
      print(*row)
  print()

def checkWin(board):
  for row in range(len(board)):
      for col in range(len(board)-1):
          if board[row][col] == "_" or board[row][col+1] == "_" or board[row][col] != board[row][col+1]:
              break
      else:
          return True
  for col in range(len(board)):
      for row in range(len(board)-1):
          if board[row][col] == "_" or board[row+1][col] == "_" or board[row][col] != board[row+1][col]:
              break
      else:
          return True
  for cell in range(len(board)-1):
      if board[cell][cell] == "_" or board[cell+1][cell+1] == "_" or board[cell][cell] != board[cell+1][cell+1]:
          break
  else:
      return True
  for cell in range(len(board)-1):
      emptyCell = board[cell][len(board)-cell-1] == "_" or board[cell+1][len(board)-cell-2] == "_"
      different = board[cell][len(board)-cell-1] != board[cell+1][len(board)-cell-2]
      if emptyCell or different:
          break
  else:
      return True
  return False
  
def play():
  print("Ваше игровое поле:")
  N = 3 
  board = [['_'] * 3 for _ in range(N)]
  used = 0
  turn = 0
  while True:
      printBoard(board)
      pick = getInput(prompt=f"Игрок {turn+1} - Введите местоположение вашей фигуры (строка пробел столбик): ",
                      cast=lambda line: tuple(map(int, line.split(" "))),
                      condition=lambda pair: min(pair) >= 0 and max(pair) < N and board[pair[0]][pair[1]] == "_",
                      errorMessage="Неправильный ввод. Пожалуйста, введите через пробел свбодное место для вашей фигуры.")
      board[pick[0]][pick[1]] = "X" if turn == 0 else "O"
      used += 1
      if checkWin(board):
          printBoard(board)
          print(f"Игра закончена, Игрок {turn+1} выиграл.")
          break
      elif used == N*N:
          printBoard(board)
          print("Игра закончена. Ничья.")
          break
      turn = (turn+1)%2

if __name__ == '__main__':
  play()