from django.db import models
from django.urls import reverse

class ContactsManager (models.Manager):
    def get_queryset(self):
        return super().get_queryset()

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.first_name + ' ' + self.last_name if self.last_name else self.first_name
    
    def get_absolute_url(self):
        return reverse("contact_detail", args=[self.id])
    
    class Meta:
        ordering = ['first_name']