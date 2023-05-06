from django.http.response import JsonResponse

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from .models import *
from .serializers import *

# Create your views here.
def test(req):
    return JsonResponse({"message": "test"})

# ログイン済みのユーザーのみが実行可能
class LoginRequired(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, req):
        return JsonResponse({"message": "seccess"})

# ユーザーに関する操作
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


