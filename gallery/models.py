from django.db import models

# Create your models here.
class Gallery(models.Model):
    gallery_name = models.CharField(max_length=500, default = "")
    gallery_type = models.CharField(max_length=200, default = "")
    gallery_short_details = models.CharField(max_length=2000, default = "")
    gallery_thumbnail = models.ImageField(upload_to="gallery_thumbnail")
    def __str__(self):
        return self.gallery_name
    
    

class GalleryImage(models.Model):
    gallery_name = models.ForeignKey(Gallery, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="gallery_pic")
    
    
    