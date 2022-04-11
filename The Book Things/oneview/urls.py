from django.urls import path
from . import views

urlpatterns = [
    path('oneview/<int:view_id>/',views.oneview,name='oneview'),
    path('oneview/<int:view_id>',views.bookrating,name='bookrating'),
]