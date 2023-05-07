import uuid
from django.db import models
from accounts.models import UserAccount


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    address = models.CharField(max_length=64)
    balance = models.IntegerField()
    is_parent = models.BooleanField()

# 組織(どの親にどの子が所属しているか保持する)
class Organization(models.Model):
    parent_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="parent_user")
    child_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="child_user")

# 取引履歴
# 親から子への通貨の移動を保持する
# 子が親へ通貨を支払った際は，負の数として保持する
class TreatHistory(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="from_user")
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="to_user")
    amount = models.IntegerField()