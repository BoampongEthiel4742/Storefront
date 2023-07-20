from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('view/<int:pk>', views.view, name="view"),
    path('login/', views.loginPage, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logoutUser, name="logout"),
    path('add/', views.add, name="add"),
    path('delete/<int:pk>', views.delete, name="delete"),
    path('edit/<int:pk>', views.edit, name="edit"),
]