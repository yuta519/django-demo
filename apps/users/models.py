import uuid

from django.db import models

# Create your models here.


class User:
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("ユーザ名", max_length=200)
    age = models.IntegerField("年齢", default=20)
    gender = models.CharField("性別", max_length=5)

    class Meta:
        verbose_name_plural = verbose_name = "ユーザ"
