from django.db import models

# model for each portfolio project
class Project(models.Model):
    title = models.CharField(max_length=100) # specify max number of characters
    body = models.CharField(max_length=300)
    image = models.ImageField(upload_to='homepage/images/') # requires pillow
    url = models.URLField(blank=True) # provide option for no URL

    def __str__(self): # return default name in admin page
        return self.title