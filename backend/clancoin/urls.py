from django.urls import path
from . import views

urlpatterns = [
    path('auth-test/', views.LoginRequired.as_view()),
    path('test/', views.test),
]
