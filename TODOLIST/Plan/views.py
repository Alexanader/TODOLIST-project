from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def formpage_view(*args, **kwargs):
	return HttpResponse("<h1>here a page</h1>")