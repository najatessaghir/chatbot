from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('chat/', views.chat_page, name='chat'),
    path('chat/<str:question>/', views.response, name='response'),
]