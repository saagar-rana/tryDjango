from django.urls import path
from . import views

urlpatterns =[
    path('uu/',views.setResponse,name='first')
]