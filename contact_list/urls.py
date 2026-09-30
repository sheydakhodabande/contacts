from django.urls import path
from . import views

urlpatterns = [ 
            path('', views.contact_list, name='contact_list'),
            path('contact/<slug:slug>/', views.contact_detail, name='contact_detail'),
            path('contact/create/',views.contact_create,name='contact_create'),
            ]