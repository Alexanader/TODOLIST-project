from django import forms
import datetime

from ..models import Plantodo

class PlanForm(forms.ModelForm):
	title = forms.CharField(label='',
				widget = forms.TextInput(attrs={"placeholder": "Title",
					'size': 20}))
	description = forms.CharField(label ='',
				widget = forms.TextInput(attrs={"placeholder": "Plan"}))
	start_time = forms.CharField(label='',
				widget = forms.TextInput(attrs={"placeholder": datetime.datetime.now().date() }))
	end_time = forms.CharField(label='',
				widget = forms.TextInput(attrs={"placeholder": datetime.datetime.now().date()}))
	class Meta:
		model = Plantodo
		fields =[ 
			'title',
			'description',
			'start_time',
			'end_time'
			]

