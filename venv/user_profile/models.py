from django.db import models
from django.db.models.fields import CharField,URLField
from django.db.models.fields.files import ImageField

# Create your models here.
class Project(models.Model):
    title = CharField(max_length=100)
    descriptcion = CharField(max_length=250)
    image = ImageField(upload_to="user_profile/images/")
    url = URLField(blank=True)