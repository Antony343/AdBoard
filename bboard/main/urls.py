from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('<str:page>/', views.other_page, name='other'),
    path('', views.Index.as_view(), name='index'),
    path('profile/', views.profile, name='profile'),
]
