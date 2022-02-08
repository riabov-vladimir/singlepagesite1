from django.shortcuts import render
from globals import move
from game.game3x3.Moves import Move


def game_action(request, action):
	if action == 1:
		move.action_left()
	elif action == 2:
		move.action_right()
	elif action == 3:
		move.action_up()
	elif action == 4:
		move.action_down()
	elif action == 5:
		move.pattern = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
		move.generate_tile_on_move()
		move.generate_tile_on_move()

	context = {
		'cell1': move.pattern[0][0],
		'cell2': move.pattern[0][1],
		'cell3': move.pattern[0][2],
		'cell4': move.pattern[1][0],
		'cell5': move.pattern[1][1],
		'cell6': move.pattern[1][2],
		'cell7': move.pattern[2][0],
		'cell8': move.pattern[2][1],
		'cell9': move.pattern[2][2],
	}
	return render(request,
	              'game/game.html',
	              context=context)


def game_index(request):

	context = {
		'cell1': move.pattern[0][0],
		'cell2': move.pattern[0][1],
		'cell3': move.pattern[0][2],
		'cell4': move.pattern[1][0],
		'cell5': move.pattern[1][1],
		'cell6': move.pattern[1][2],
		'cell7': move.pattern[2][0],
		'cell8': move.pattern[2][1],
		'cell9': move.pattern[2][2],
	}
	return render(request,
	              'game/game.html',
	              context=context)


