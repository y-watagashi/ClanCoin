from rest_framework import permissions
import requests

class OwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        token = request.headers['Authorization']
        url = "http://localhost:8000/api/auth/users/me/"
        headers = {
        'Authorization': f'{token}'
        }
        response = requests.request("GET", url, headers=headers)
        user_id = response.json()['id']
        return obj.user == user_id