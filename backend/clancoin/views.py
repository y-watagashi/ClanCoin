import requests
from django.db.models import Q
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


# 取引履歴の操作
class TreatHistoryViewSet(viewsets.ModelViewSet):
    queryset = TreatHistory.objects.all()
    serializer_class = TreatHistorySerializer
    permission_classes = [IsAuthenticated]

    # JWTのユーザーに関連する取引の取得
    def list(self, req):
        user = User.objects.filter(user=req.user).first()
        treats = TreatHistory.objects.filter(Q(to_user = user) | Q(from_user = user))
        for obj in treats:
            print(obj.context)
        return Response({"treats": treats.values('from_user', 'to_user', 'amount')})

    # 取引の追加
    def create(self, req):
        # JWTの情報からユーザーを取得
        user_id = User.objects.filter(user=req.user).first().id
        
        data = {
            "from_user": int(req.POST.get('from_user', None)),
            "to_user": int(req.POST.get('to_user', None)),
            "amount": int(req.POST.get('amount'))
        }
        
        serializer = self.serializer_class(data=data)

        # JWTのユーザーからの送信以外の追加は行えない
        if user_id != data['from_user']:
            return Response(data = {"message": "cant add data"}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data = serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]

    def list(self, req):
        user = User.objects.filter(user=req.user).first()
        if not user.is_parent:
            return Response({"permission denied"}, status=status.HTTP_401_UNAUTHORIZED)
        organization = Organization.objects.filter(parent_user=user)
        return Response({"organization": organization.values('child_user')})
