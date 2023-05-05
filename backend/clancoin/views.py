from django.http.response import JsonResponse

# Create your views here.
def test(req):
    return JsonResponse({"message": "test"})