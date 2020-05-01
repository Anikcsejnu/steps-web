from django.db import models
from django.utils import timezone

# Create your models here.

class Events(models.Model):
	event_title = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	date = models.DateField(max_length=8, default=timezone.now)
	time = models.TimeField()
	enrty_fee = models.IntegerField()

	banner = models.ImageField(default='default.jpg', upload_to='events_banner')


	def __str__(self):
		return self.event_title

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		img = Image.open(self.image.path)

		if img.height > 345 or img.width > 690:
			#output_size = (418, 371)
			img = img.resize((690, 345), Image.ANTIALIAS)
			# img.thumbnail(output_size)
			img.save(self.image.path)