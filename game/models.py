from django.db import models


class GameState(models.Model):
	session_key = models.CharField(max_length=500, unique=True)
	cell1 = models.IntegerField(default=0)
	cell2 = models.IntegerField(default=0)
	cell3 = models.IntegerField(default=0)
	cell4 = models.IntegerField(default=0)
	cell5 = models.IntegerField(default=0)
	cell6 = models.IntegerField(default=0)
	cell7 = models.IntegerField(default=0)
	cell8 = models.IntegerField(default=0)
	cell9 = models.IntegerField(default=0)
	created = models.DateTimeField(auto_now_add=True, verbose_name='Date created')
	updated = models.DateTimeField(auto_now=True, verbose_name='Date updated')


	class Meta:
		ordering = ('-created',)
		verbose_name = 'Game state'
		verbose_name_plural = 'Game states by sessions'

	def __str__(self):
		return f'Game state for session {self.session_key}'
