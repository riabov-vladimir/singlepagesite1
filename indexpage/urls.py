from django.urls import path
from indexpage.views import *

urlpatterns = [
	path('', index_page, name='index'),
	path('cv', cv_page, name='cv'),
	# path('game', game_page, name='game'),
	path('cat', cat_page, name='cat')
]