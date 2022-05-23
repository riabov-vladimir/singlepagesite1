from django.db import models
from datetime import datetime

from django.template.backends import django


class CvText(models.Model):
    is_html = models.BooleanField(null=False)
    cv_text = models.TextField(null=False)
    last_modified = models.DateTimeField(auto_now=True)

