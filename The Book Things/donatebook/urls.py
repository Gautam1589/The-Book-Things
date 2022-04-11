from django.urls import path
from . import views

urlpatterns = [
    path('',views.bookdonate,name='bookdonate'),
    
]