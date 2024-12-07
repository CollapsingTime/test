from django.db import models

class Developer(models.Model):
    title = models.CharField("Articul", max_length=32)

    class Meta:
        verbose_name = "Developer"
        verbose_name_plural = "Developers"