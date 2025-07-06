from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    subscription_status = models.CharField(max_length=50)

    def __str__(self):
        return self.name


