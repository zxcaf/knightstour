#!/usr/bin/python3

from random import randint

def PrintBoard(inBoard, dim_h):

	for i in range(dim_h):
		print(inBoard[i])
	
	print("")


# Constants
w, h = 8, 8
Moves = [(-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, 2), (2, 1), (2, -1), (1, -2)]
#Slot = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63" ]

gamecnt = 0
compcnt = 0
while True:

	# new Board
	Board = [["XX" for x in range(w)] for y in range(h)]

	# random position on board
	y = randint(0,7)
	x = randint(0,7)
	Board[y][x] = "01"
	gamecnt += 1

	if gamecnt % 100000 == 0:
		print("Game Count:", gamecnt)

	vms = 7
	mv_num = 2
	while vms >= 0:

		idx = randint(0, vms)
		mv_y, mv_x = Moves[idx]
		new_x = x + mv_x
		new_y = y + mv_y

		if 0 <= new_x < 8 and 0 <= new_y < 8 and Board[new_y][new_x] == "XX":

			x, y = new_x, new_y
			
			# Slot method, easy here, requries all the constants up there
			# Board[y][x] = Slot[mv_num]

			if mv_num < 10:
					bVal = "0" + str(mv_num)
			else:
				bVal = str(mv_num)

			Board[y][x] = bVal

			vms = 7
			mv_num += 1
			if mv_num > 64:
				compcnt += 1
				print("Game Count:", gamecnt)
				print("Complete Count:", compcnt)
				print
				PrintBoard(Board,h)
				break

		else:
			vms = vms - 1
			inval_mv = Moves.pop(idx)
			Moves.append(inval_mv)
