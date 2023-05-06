import requests

from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import viewsets

from .models import *
from .serializers import *
from .permissions import *

def test(req):
    return JsonResponse({"hello": "hello"})

# ログイン済みのユーザーのみが実行可能
class LoginRequired(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, req):
        return JsonResponse({"message": "seccess"})


# ユーザーに関する操作
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    # Headerに含まれるJWTに対応するユーザーのみを表示する
    def list(self, req):
        return Response({'user': User.objects.filter(user=req.user).values('id', 'address')})



# 組織に関する操作
class OrganizationViewSet(viewsets.ModelViewSet):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()

    def list(self, req):
        organization = Organization.objects.filter(
            parent_user = req.query_params.get('parent_user_id')
        )
        print(organization)
        return Response({"organization": organization}, status=status.HTTP_200_OK)