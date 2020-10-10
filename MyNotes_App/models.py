from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MyNotes_Model(models.Model): 
    notes_title = models.CharField(max_length=100, null=True, blank=True)
    notes_description = models.TextField()
    notes_created_date = models.DateField()
    notes_favorite = models.BooleanField(blank=True, default=False)
    notes_archived = models.BooleanField(blank=True, default=False)
    notes_username = models.CharField(max_length=150, default='Yathindra')