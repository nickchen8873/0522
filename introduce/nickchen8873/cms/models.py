from __future__ import unicode_literals
from django.db import models

# Create your models here.

class me(models.Model):
	name = models.CharField(max_length=20)
	Id_number = models.CharField(max_length=15)
	address = models.CharField(max_length=50, blank=True)


	def __str__(self):
		return self.name