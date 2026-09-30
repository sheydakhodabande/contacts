from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class ContactsManager (models.Manager):
    def get_queryset(self):
        return super().get_queryset()

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    slug = models.SlugField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.first_name + ' ' + self.last_name if self.last_name else self.first_name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            name = self.first_name
            if self.last_name:
                name += '-' + self.last_name
            self.slug = slugify(name)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("contact_detail", args=[self.slug])
    
    class Meta:
        ordering = ['first_name']