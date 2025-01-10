#!/usr/bin/python3

from random import randint
from time import sleep

# Constants
w = 8
h = 8
Moves = [(-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, 2), (2, 1), (2, -1), (1, -2)]

# Init
gamecnt = 0
compcnt = 0
max_mvs = 40

# Functions

# Print the current board state
def PrintBoard(inBoard, dim_h):

	for i in range(dim_h):
		print(inBoard[i])
	
	print("")


# get all valid moves from a specific location
def validMoves(inX, inY, inBoard):

	validMvs = []

	# nomenclature "t" test, "m" move, "in" input
	for tY, tX in Moves:
		mX = inX + tX
		mY = inY + tY

		if 0 <= mX < 8 and 0 <= mY < 8 and Board[mY][mX] == "XX":
			validMvs.append((mX, mY))

	return validMvs


# main
while True:

	# Per attempt init
	Board = [["XX" for x in range(w)] for y in range(h)]
	gamecnt += 1
	mv_num = 1

	# random position on board
	y = randint(0,7)
	x = randint(0,7)
	Board[y][x] = "01"

	# worry dots
	if gamecnt % 100000 == 0:
		print("Game Count:", gamecnt)

	# per move action
	while True:

		mvList = validMoves(x, y, Board)

		if len(mvList) == 0:		# we are done
			break

		elif len(mvList) == 1:		# take what we have got
			x, y = mvList[0]

		elif len(mvList) > 1:

			chkList = []
			for i, j in mvList:
				tmpList = validMoves(i, j, Board)
				z = len(tmpList)
				chkList.append((z, (i, j)))

			chkList.sort(key=lambda tup: tup[0], reverse=True)

			max = chkList[0][0]

			i = j = 0
			while i < len(chkList):

				if i == max:
					j += 1			# counts the number of the highest value
				i += 1


			x, y = chkList[randint(0, j)][1]

		mv_num += 1
		if mv_num < 10:
				bVal = "0" + str(mv_num)
		else:
			bVal = str(mv_num)

		Board[y][x] = bVal

		if mv_num > max_mvs:
			max_mvs = mv_num
			print("Game Count:", gamecnt)
			print("Move Count:", mv_num)
			PrintBoard(Board,h)

		if mv_num >= 64:
			print("Game Count:", gamecnt)
			PrintBoard(Board,h)
			break
