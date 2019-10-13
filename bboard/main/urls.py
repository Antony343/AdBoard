from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('<str:page>/', views.other_page, name='other'),
    path('', views.Index.as_view(), name='index'),
    path('profile/delete', views.DeleteUserView.as_view(), name='profile_delete'),
    path('profile/update', views.ChangeUserInfoView.as_view(), name='profile_update'),
    path('profile/', views.profile, name='profile'),
    path('accounts/signup/done', views.SignUpDoneView.as_view(), name='sign_up_done'),
    path('accounts/signup/activate/<str:sign>/', views.user_activate, name='sign_up_activate'),
    path('accounts/signup/', views.SignUpUserView.as_view(), name='sign_up'),

]
