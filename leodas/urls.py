from django.urls import path
from  . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('hello/',views.html,name='html'),
    path('lcu/',views.lcu,name='lcu'),
    path('lcu1/',views.lcu1,name='lcu1')
]
