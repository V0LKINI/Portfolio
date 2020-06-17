from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	date = models.DateField()

	def brief_text(self):
		return self.description[0:50]


	
