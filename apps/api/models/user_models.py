import uuid

from django.db import models


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("ユーザ名", max_length=200)
    age = models.IntegerField("年齢", default=20)
    gender = models.CharField("性別", max_length=5)

    class Meta:
        verbose_name = 'ユーザ'
        verbose_name_plural = 'ユーザ'
        db_table = 'users'

    def __str__(self) -> str:
        return self.name
