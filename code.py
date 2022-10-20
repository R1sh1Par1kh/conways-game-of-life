import time

grid = []
for i in range(20):
  line = []
  for j in range(20):
    line.append(False)
  grid.append(line)
  
f = open("test.in")
lines = f.readlines()
lines = [line.strip() for line in lines]


for item in lines:
  coords = [int(x) for x in item.split()]
  grid[coords[0]][coords[1]] = True
  
def printBoard(game):
  for r in range(len(game)):
    for c in range(len(game[0])):
      if game[r][c] == False:
        print("-", end = "")
      else:
        print("o", end = "")
    print()    

def neighbors(game, r, c):
  aliveCounter = 0
  
  if r-1 >= 0 and c-1 >= 0 and game[r-1][c-1]:
    aliveCounter += 1
  if r-1 >= 0 and game[r-1][c]:
    aliveCounter += 1
  if r-1 >= 0 and c+1 < len(game[0]) and game[r-1][c+1] == True:
    aliveCounter += 1
  if c-1 >= 0 and game[r][c-1] == True:
    aliveCounter += 1
  if c+1 < len(game[0]) and game[r][c+1] == True:
    aliveCounter += 1
  if r+1 < len(game) and c-1 >= 0 and game[r+1][c-1] == True:
    aliveCounter += 1
  if r+1 < len(game) and game[r+1][c] == True:
    aliveCounter += 1
  if r+1 < len(game) and c+1 < len(game[0]) and game[r+1][c+1] == True:
    aliveCounter += 1
  
  if aliveCounter < 2 and game[r][c]:
    return False
  elif aliveCounter < 4 and game[r][c]:
    return True
  elif game[r][c]:
    return False
  if aliveCounter == 3 and game[r][c] == False:
    return True
  return False


input("Welcome to Conway's Game of Life. We start with a 30x58 grid \nof cells, either alive or dead. Here are the rules:\n\t1) Any live cell with fewer than two live neighbors \n\t   dies, as if by underpopulation.\n\t2) Any live cell with two or three live neighbors \n\t   lives on to the next generation.\n\t3) Any live cell with more than three live neighbors \n\t   dies, as if by overpopulation.\n\t4) Any dead cell with exactly three live neighbors \n\t   becomes a live cell, as if by reproduction.\nPress Enter to continue:")

printBoard(grid)

input("Press Enter to continue:")

while True:
  newGrid = []
  for i in range(20):
    line = []
    for j in range(20):
      line.append(False)
    newGrid.append(line)
    
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      newGrid[r][c] = neighbors(grid, r, c)
  printBoard(newGrid)
  grid = newGrid
  time.sleep(.5)
