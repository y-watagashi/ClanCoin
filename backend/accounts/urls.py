from django.urls import path
from .views import UserList, activate_user

urlpatterns = [
    path('users/', UserList.as_view()),
    path('activate/<str:uid>/<str:token>', activate_user),

]