from django.urls import path
from mainpage import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about' ),
    path('detail/', views.detail, name='detail')
]