from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('activate/<str:uid>/<str:token>', views.activate_user),
]