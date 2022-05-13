import datetime
from django.views.generic.base import TemplateView


class CatView(TemplateView):
	template_name = 'indexpage/cat.html'

	def get_context_data(self):
		context = {'is_index': False}
		return context


class IndexView(TemplateView):
	template_name = 'indexpage/index.html'
	now = str(datetime.datetime.now())

	def get_context_data(self):
		context = {
			'is_index': True,
			'now': self.now
		}
		return context


class CvView(TemplateView):
	template_name = 'indexpage/cv.html'

	def get_context_data(self):
		context = {'is_index': False}
		return context
