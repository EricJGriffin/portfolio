from django.db import models

# Create your models here.
class Proj(models.Model):
	image = models.ImageField(upload_to='image/', blank=True, null=True)
	title = models.CharField(max_length=120)
	content = models.TextField(null=True, blank=True)