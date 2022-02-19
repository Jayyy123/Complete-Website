from django.urls import path
from . import views


urlpatterns = [
    path('', views.authenticationPage, name = 'authenticationPage'),
    path('loginPage/', views.loginPage, name = 'loginPage'),
    path('logoutPage/', views.logoutPage, name = 'logoutPage'),
    path('signupPage/', views.signupPage, name = 'signupPage'),
    path('profile/', views.profile, name='profile'),
    path('account/<str:pk>/', views.account, name='account'),
    path('edit_profile/<str:pk>/', views.edit_profile, name='edit_profile')

]