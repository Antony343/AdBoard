from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [

    path('profile/delete', views.DeleteUserView.as_view(), name='profile_delete'),
    path('profile/update', views.ChangeUserInfoView.as_view(), name='profile_update'),
    path('profile/add/', views.profile_bb_add, name='profile_bb_add'),
    path('profile/update/<int:pk>/', views.profile_bb_change, name='profile_bb_change'),
    path('profile/delete/<int:pk>', views.profile_bb_delete, name='profile_bb_delete'),
    path('profile/<int:pk>/', views.profile_bb_detail, name='profile_bb_detail'),
    path('profile/', views.profile, name='profile'),
    path('accounts/signup/done', views.SignUpDoneView.as_view(), name='sign_up_done'),
    path('accounts/signup/activate/<str:sign>/', views.user_activate, name='sign_up_activate'),
    path('accounts/signup/', views.SignUpUserView.as_view(), name='sign_up'),
    path('<int:rubric_pk>/<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/', views.by_rubric, name='by_rubric'),
    path('<str:page>/', views.other_page, name='other'),
    path('', views.Index.as_view(), name='index'),
]
