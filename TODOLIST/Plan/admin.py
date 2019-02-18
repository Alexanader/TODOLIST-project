from django.contrib import admin
from django.urls import reverse

from .models import Plantodo

class FormAdmin(admin.ModelAdmin):
	list_display = ['title', 'start_time', 'end_time', 'Post_time']
	list_display_links  = ['title']
	list_per_page = 5
	search_fields = ['title', 'start_time', 'end_time', 'Post_time']

	def view_on_site(self, object):
		return reverse('form_edit', kwargs = {'pk': object.id})

admin.site.register(Plantodo, FormAdmin)

# Register your models here.
