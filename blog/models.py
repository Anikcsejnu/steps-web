from django.db import models
from PIL import Image
from django.utils import timezone
# Create your models here.

class Blog(models.Model):
	name = models.CharField(max_length=100)
	institute = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	content = models.TextField()
	status = models.BooleanField(default=False)
	date = models.DateField(default=timezone.now)
	time = models.TimeField(auto_now=True)

	image = models.ImageField(default='blog_pic/default.jpg', upload_to='blog_pic')
	
	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		img = Image.open(self.image.path)
		if img.height > 418 or img.width > 371:
			#output_size = (418, 371)
			img = img.resize((371, 418), Image.ANTIALIAS)
			# img.thumbnail(output_size)
			img.save(self.image.path)
