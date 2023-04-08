from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('signin/', views.login_page, name='signin'),
    path('logout/', views.logout_profile, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('complete_profile/', views.complete_profile, name='complete_profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]
