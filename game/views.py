from django.shortcuts import render
# from globals import move
from game.game3x3.Moves import Move
from game.models import GameState
from django.core.exceptions import ObjectDoesNotExist
"""
Короче действуем так:

При вызове вьюшки смотрим в базе есть ли модель GameState с полем session_key равным 
собственно ключу конкретной сессии под которой пользователь эту вьюшку вызвал.
1) Если есть, то пользуемся значениями из данной модельки.
2) Если нет, то создаем новый экземпляр и работаем с ним. Таким образом дальнейший ход игры будет всегда обращаться
к пунтку 1.
"""

def game_action(request, action):

	try:
		game_state = GameState.objects.get(session_key=request.session.session_key)
		move = Move(game_state=game_state)
	except ObjectDoesNotExist:
		game_state = GameState.objects.create(session_key=request.session.session_key)
		move = Move(game_state=game_state)
		move.generate_tile_on_move()
		move.generate_tile_on_move()

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

	record_move = GameState.objects.get(session_key=request.session.session_key)
	a = record_move
	record_move.cell1 = int(move.pattern[0][0]),
	record_move.cell2 = int(move.pattern[0][1]),
	record_move.cell3 = int(move.pattern[0][2]),
	record_move.cell4 = int(move.pattern[1][0]),
	record_move.cell5 = int(move.pattern[1][1]),
	record_move.cell6 = int(move.pattern[1][2]),
	record_move.cell7 = int(move.pattern[2][0]),
	record_move.cell8 = int(move.pattern[2][1]),
	record_move.cell9 = int(move.pattern[2][2])

	record_move.save()

	game_state.cell1 = move.pattern[0][0]
	game_state.cell2 = move.pattern[0][1]
	game_state.cell3 = move.pattern[0][2]
	game_state.cell4 = move.pattern[1][0]
	game_state.cell5 = move.pattern[1][1]
	game_state.cell6 = move.pattern[1][2]
	game_state.cell7 = move.pattern[2][0]
	game_state.cell8 = move.pattern[2][1]
	game_state.cell9 = move.pattern[2][2]

	game_state.save()


	context = {
		'cell1': move.pattern[0][0],
		'cell2': move.pattern[0][1],
		'cell3': move.pattern[0][2],
		'cell4': move.pattern[1][0],
		'cell5': move.pattern[1][1],
		'cell6': move.pattern[1][2],
		'cell7': move.pattern[2][0],
		'cell8': move.pattern[2][1],
		'cell9': move.pattern[2][2]
	}
	return render(request,
	              'game/game.html',
	              context=context)


# def game_index(request):
# 	"""
# 	obj, created = Person.objects.get_or_create(first_name='John', last_name='Lennon',
# 	                  defaults={'birthday': date(1940, 10, 9)})
# 	"""
# 	try:
# 		game_state = GameState.objects.get(session_key=request.session.session_key)
# 		move = Move(game_state=game_state)
# 	except ObjectDoesNotExist:
# 		game_state = GameState.objects.create(session_key=request.session.session_key)
# 		move = Move(game_state=game_state)
# 		move.generate_tile_on_move()
# 		move.generate_tile_on_move()
#
# 	context = {
# 		'cell1': move.pattern[0][0],
# 		'cell2': move.pattern[0][1],
# 		'cell3': move.pattern[0][2],
# 		'cell4': move.pattern[1][0],
# 		'cell5': move.pattern[1][1],
# 		'cell6': move.pattern[1][2],
# 		'cell7': move.pattern[2][0],
# 		'cell8': move.pattern[2][1],
# 		'cell9': move.pattern[2][2],
# 	}
#
# 	return render(request,
# 	              'game/game.html',
# 	              context=context)


def game_index(request):
	"""
	obj, created = Person.objects.get_or_create(first_name='John', last_name='Lennon',
	                  defaults={'birthday': date(1940, 10, 9)})
	"""

	if not request.session.session_key:
		request.session.create()
	session_id = request.session.session_key

	try:
		game_state = GameState.objects.get(session_key=request.session.session_key)
		object_exists = True
	except ObjectDoesNotExist:
		object_exists = False

	if object_exists:
		move = Move()

		move.pattern = [
			[game_state.cell1, game_state.cell2, game_state.cell3],
			[game_state.cell4, game_state.cell5, game_state.cell6],
			[game_state.cell7, game_state.cell8, game_state.cell9]
		]
		print(move)
	else:
		game_state = GameState.objects.create(session_key=request.session.session_key)
		move = Move()
		print(move)
		game_state.cell1 = move.pattern[0][0]
		game_state.cell2 = move.pattern[0][1]
		game_state.cell3 = move.pattern[0][2]
		game_state.cell4 = move.pattern[1][0]
		game_state.cell5 = move.pattern[1][1]
		game_state.cell6 = move.pattern[1][2]
		game_state.cell7 = move.pattern[2][0]
		game_state.cell8 = move.pattern[2][1]
		game_state.cell9 = move.pattern[2][2]

		game_state.save()

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