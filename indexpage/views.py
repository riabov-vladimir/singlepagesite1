import datetime
from django.shortcuts import render


def index_page(request):
	now = str(datetime.datetime.now())
	return render(request, 'indexpage/index.html', context={'now': now})


def cv_page(request):
	return render(request, 'indexpage/cv.html')


def cat_page(request):
	return render(request, 'indexpage/cat.html')
