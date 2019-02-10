from django.shortcuts import render
from django.http import HttpResponse

from .models import Plantodo

from .forms.formadd import PlanForm

# Create your views here.
def formpage_view(request, *args, **kwargs):
	obj = Plantodo.objects.get(id=11)
	context = { 
		'object': obj
	}
	return render(request,"form/show_all_form.html", context) 

def formpage_create_view(request):
	form = PlanForm(request.POST or None)
	if form.is_valid():
		form.save()

	context = {
		'form': form
	}
	return render(request,"form/addform.html",context)

def formpage_show_all_view(request):
	pass

def homepage_view(request,*args,**kwargs):
	return render(request,"home.html",{}) 