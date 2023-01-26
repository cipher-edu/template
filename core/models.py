from django.db import models

# Create your models here.
class LandingHead(models.Model):
    logos = models.ImageField(upload_to='logo/')
    landing_image = models.ImageField(upload_to='images/')
    landing_title = models.TextField(max_length=250)

    # def __init__(self):
    #     return self.landing_title