from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView
from .serializers import UserSerializer

from django.http.response import JsonResponse
import requests
from rest_framework import status


User = get_user_model()

class UserList(ListAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer

def activate_user(req, uid, token):
    # アカウントをアクティベートする
    request_body = {'uid':uid, 'token':token}
    response = requests.post("http://localhost:8000/api/auth/users/activation/", json=request_body)
    # uidもしくはtokenが誤っている際は，エラーを返す
    if response.status_code == 400:
        return JsonResponse({"message": "incorrect uid or token"}, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({"message": "account is activated"})