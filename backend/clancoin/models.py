from django.db import models
from accounts.models import UserAccount

# 親ユーザー
class ParentUser(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)

# 子供ユーザー
class ChildUser(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    balance = models.IntegerField()

# 組織(どの親にどの子が所属しているか保持する)
class Organization(models.Model):
    parent_user = models.ForeignKey(ParentUser, on_delete=models.CASCADE)
    child_user = models.ForeignKey(ChildUser, on_delete=models.CASCADE)

# 取引履歴
# 親から子への通貨の移動を保持する
# 子が親へ通貨を支払った際は，負の数として保持する
class TreatHistory(models.Model):
    parent_user = models.ForeignKey(ParentUser, on_delete=models.CASCADE)
    child_user = models.ForeignKey(ChildUser, on_delete=models.CASCADE)
    amount = models.IntegerField()
    