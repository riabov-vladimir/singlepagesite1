from django.urls import path
from indexpage.views import *

urlpatterns = [
	path('', IndexView.as_view(), name='index'),
	path('cv', CvView.as_view(), name='cv'),
	path('cat', CatView.as_view(), name='cat')
]
