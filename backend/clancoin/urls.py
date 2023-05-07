from django.urls import path
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('organization', OrganizationViewSet)
router.register('treat-history', TreatHistoryViewSet)


urlpatterns = router.urls

urlpatterns += [
    path('test/', test),
]