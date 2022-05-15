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

    def get_age(self):
        date_1 = '17/05/1988 13:13:08.230010'
        date_format_str = '%d/%m/%Y %H:%M:%S.%f'
        diff = datetime.datetime.now() - datetime.datetime.strptime(date_1, date_format_str)
        return int(diff.total_seconds())

    def get_context_data(self):
        context = {'is_index': False,
                   'age': self.get_age()}
        return context
