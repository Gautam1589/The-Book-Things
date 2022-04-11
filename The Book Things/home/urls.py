from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    # path('<cate>/',views.catfun,name='catfunction')
    # path('oneview/',views.oneview,name='oneviewname'),
    
]