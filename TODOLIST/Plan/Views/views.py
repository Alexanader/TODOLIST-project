from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse
from django.forms import ModelForm

from ..models import Plantodo

from ..forms.formadd import PlanForm

# Create your views here.

@login_required
def formpage_create_view(request):
	if request.method == 'POST':
		form_add = PlanForm(request.POST or None)
		if form_add.is_valid():
			fields = form_add.cleaned_data
			fields['user'] = request.user
			plan = Plantodo(**fields)
			plan.save()
		return redirect('form')
	else:
		return render(request, "form/addform.html", {'form':PlanForm()})

@login_required
def formpage_show_all_view(request, *args, **kwargs):
	#if request.user.is_authenticated:
	obj = Plantodo.objects.filter(user=request.user).order_by('end_time')
	context =({ 
		'objects': obj
	})
	#else:
	#	return HttpResponseForbidden()
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

