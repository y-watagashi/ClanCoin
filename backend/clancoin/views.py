from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


# Create your views here.
def test(req):
    return JsonResponse({"message": "test"})

# ログイン済みのユーザーのみが実行可能
class LoginRequired(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, req):
        return JsonResponse({"message": "seccess"})