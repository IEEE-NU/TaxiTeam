from django.db import models

class Group(models.Model):
	date = models.DateTimeField()
	start_location = models.TextField()
	destination = models.TextField()
	time = models.DateTimeField()
	num_ppl = models.IntegerField()
	