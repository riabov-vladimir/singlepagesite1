import datetime
from django.shortcuts import render


def index_page(request):
	print('--------index page----------')
	now = str(datetime.datetime.now())
	return render(request, 'indexpage/index.html', context={'now': now})


def cv_page(request):
	return render(request, 'indexpage/cv.html')


# def game_page(request):
# 	return render(request, 'indexpage/game.html')


def cat_page(request):
	return render(request, 'indexpage/cat.html')
