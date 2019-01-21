from django.db import models

# Create your models here.
class Permission(models.Model):
    class Meta:
        # 权限信息
        permissions = (
            ('views_register_user', '')
        )