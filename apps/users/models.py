import uuid
from django.db import models

# Create your models here.


class User:
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("会社名", max_length=200)
    term_month = models.IntegerField("決算月", default=3)
    sales_prospects = models.IntegerField("見込み売上", default=0)

    class Meta:
        verbose_name_plural = verbose_name = "会社"
