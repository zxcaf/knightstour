#!/usr/bin/python3

from random import randint
from time import sleep

def PrintBoard(inBoard, dim_h):

	for i in range(dim_h):
		print(inBoard[i])
	
	print("")


# Constants
w, h = 8, 8
Moves = [(-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, 2), (2, 1), (2, -1), (1, -2)]
gamecnt = 0
max_mv = 0
compcnt = 0 

while True:

	# new Board
	Board = [["XX" for x in range(w)] for y in range(h)]

	# random position on board
	y = randint(0,7)
	x = randint(0,7)
	Board[y][x] = "01"
	gamecnt += 1
	mv_num = 2

	if gamecnt % 100000 == 0:
		print("Game Count:", gamecnt)

	while True:

		vMlen = 0
		vMoves = []

		for ty, tx in Moves:
			mx = x + tx 
			my = y + ty

			if 0 <= mx < 8 and 0 <= my < 8 and Board[my][mx] == "XX":
				vMoves.append((my, mx))

		vMlen = len(vMoves)

		if vMlen > 0:
			mv = randint(0, vMlen - 1)
			y, x = vMoves[mv]
			mv_num += 1

			if mv_num < 10:
					bVal = "0" + str(mv_num)
			else:
				bVal = str(mv_num)

			Board[y][x] = bVal

			#if mv_num > max_mv:
			#	max_mv = mv_num
			#	if gamecnt > 2:
			#		print("Game Count, Max Moves:", gamecnt, max_mv)
			#		PrintBoard(Board, h)

			if mv_num > 64:
				compcnt += 1
				print("Game Count:", gamecnt)
				print("Complete Count:", compcnt)
				PrintBoard(Board,h)
				break
		else:
			break
