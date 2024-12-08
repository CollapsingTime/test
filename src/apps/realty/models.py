from django.db import models
from apps.developers.models import Developer

class Flat(models.Model):
    article = models.CharField("Articul", max_length=32)
    area = models.FloatField("Square",)
    price = models.IntegerField("Price", default=0, blank=True)
    developer = models.ForeignKey(
        Developer,
        verbose_name="Developer",
        related_name="flats",
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    class Meta:
        app_label = 'realty'
        indexes = [models.Index(fields=["article"])]
        verbose_name = "Flat"
        verbose_name_plural = "Flats"