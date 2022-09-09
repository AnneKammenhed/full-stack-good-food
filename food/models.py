from django.db import models


# Model for the guest contact info
class Guest(models.Model):
    guest_name = models.CharField(max_length=25, blank=True)
    guest_email = models.EmailField(blank=False)
    guest_phone = models.CharField(max_length=25, blank=True)

    def __str__(self):
        return f'{self.guest_name}'
