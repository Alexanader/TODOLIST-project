# -*- coding: utf-8 -*- 
from django.db import models


class Plantodo(models.Model):
	"""AIM model"""
	title = models.CharField(max_length = 120,
							blank = False
							)
	description = models.TextField(blank=False,
							)
	start_time = models.DateField(blank=False,null=True)
	end_time = models.DateField(blank=False, null=True)
	Post_time = models.DateField(auto_now_add=True, null=True)
	#build_time = models.TimeField()

# Create your models here.
