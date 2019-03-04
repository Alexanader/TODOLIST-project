"""TODOLIST URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from Plan.Views.views import formpage_show_all_view, formpage_create_view, homepage_view, formpage_edit_view, formpage_delete_view
from Plan.Views.registration import sign_up, log_in, log_out



urlpatterns = [
    #Forms for forms
    url(r'^$',homepage_view, name='home'),
	url(r'^form/all',formpage_show_all_view, name='form'),

    #Forms for creating, editing and deleting    
    url(r'^form/create',formpage_create_view, name='create'),
    url(r'^form/(?P<pk>\d+)/edit/$',formpage_edit_view.as_view(), name='form_edit'),
    url(r'^form/(?P<pk>\d+)/delete/$',formpage_delete_view.as_view(), name='form_delete'),


    #Form for Sing up/registration
    url(r'^signup/$', sign_up, name='sign_up'),
    url(r'^login/$', log_in, name='log_in'),
    url(r'^logout/$', log_out, name='log_out'),


    # Admin site 
    url('admin/', admin.site.urls),
]
 