from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import UpdateView, DeleteView
from django.urls import reverse
from django.forms import ModelForm

from ..models import Plantodo

from ..forms.formadd import PlanForm

# Create your views here.

def formpage_create_view(request):
	form_add = PlanForm(request.POST or None)
	if form_add.is_valid():
		form_add.save()
	context = {
		'form': form_add
	}
	return render(request,"form/addform.html",context)

def formpage_show_all_view(request, *args, **kwargs):
	obj = Plantodo.objects.all()
	context =({ 
		'objects': obj
	})
	return render(request,"form/show_all_form.html", context) 

class formpage_edit_view(UpdateView):
	fields = '__all__'
	model = Plantodo
	template_name = 'form/editform.html'
	
	def get_success_url(self,*args,**kwargs):
		return '%s?status_message=Your plan is successufully changed' % reverse('home')

	def post(self, request, *args, **kwargs):
		if request.POST.get('cancel_button'):
			return HttpResponseRedirect('%s?status_message=Редагування студента відмінено!'%reverse('home'))
		else:
			return super(formpage_edit_view, self).post(request, *args, **kwargs)

class formpage_delete_view(DeleteView):
	model = Plantodo
	template_name = 'form/deleteform.html'

	def get_success_url(self):
		return u'%s?status_message = Your plan is successufully delete' % reverse('home')
	

def homepage_view(request,*args,**kwargs):
	return render(request,"home.html",{}) 

def formpage_contact_admin_view(request):
	return render(request,"contact_admin/form.html", {})

