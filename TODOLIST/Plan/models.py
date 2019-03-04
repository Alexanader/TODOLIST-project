# -*- coding: utf-8 -*- 
from django.db import models
from django.contrib.auth.models import User

class Plantodo(models.Model):
	"""PlanTODO model"""
	user = models.ForeignKey(User,
							 blank=True,
							 null=True,
							 on_delete=models.CASCADE)
	title = models.CharField(max_length = 120,
							blank = False
							)
	description = models.TextField(blank=False,
							)
	start_time = models.DateField(blank=False,null=True)
	end_time = models.DateField(blank=False, null=True)
	Post_time = models.DateField(auto_now_add=True, null=True)
	#build_time = models.TimeField()


	def __unicode__(self):
		return self.title
# Create your models here.
	