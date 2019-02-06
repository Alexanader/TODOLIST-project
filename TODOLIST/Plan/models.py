from django.db import models


class Plantodo(models.Model):
	title = models.CharField(max_length = 120)
	description = models.TextField(blank=True, default ='some staff to do' )
	start_time = models.DateField(auto_now_add=True)
	#build_time = models.TimeField()

# Create your models here.
