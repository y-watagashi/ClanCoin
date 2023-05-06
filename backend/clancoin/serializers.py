from .models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'user',
            'address',
            'balance',
            'is_parent'
        )


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = (
            'parent_user',
            'child_user'
        )


class TreatHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TreatHistory
        fields = "__all__"