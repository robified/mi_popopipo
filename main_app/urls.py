from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('show/', views.show, name='show'),
    path('show/new', views.show.new, name='new'),
    path('show/edit', views.show.edit, name='edit'),
    path('login/', views.login, name='login'),

]