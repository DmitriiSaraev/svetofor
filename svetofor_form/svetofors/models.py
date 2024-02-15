from django.db import models


class Svetofor(models.Model):
    ip_sv = models.CharField(
        max_length=15,
        verbose_name='ip address',
    )
