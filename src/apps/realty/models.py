from django.db import models

class Flat(models.Model):
    article = models.CharField("Articul", max_length=32)
    area = models.FloatField("Square",)
    price = models.IntegerField("Price", default=0, blank=True)
    developer = models.ForeignKey(
        'developers.Developer',
        verbose_name="Developer",
        related_name="flats",
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    class Meta:
        indexes = [models.Index(fields=["article"])]
        verbose_name = "Flat"
        verbose_name_plural = "Flats"