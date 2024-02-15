from django.db import models


class Svetofor(models.Model):
    ip_address = models.CharField(
        max_length=15,
        verbose_name='ip address',
    )
    local = models.CharField(max_length=30)
    protocol = models.CharField(max_length=30)

