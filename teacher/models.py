from django.db import models
from django import forms
from django.utils import timezone
import datetime
from PIL import Image
from django_mysql.models import ListTextField, ListCharField

# Create your models here.

DEPARTMENT_CHOICES = (
    ('science','SCIENCE'),
    ('business studies', 'BUSINESS STUDIES'),
    ('english', 'ENGLISH'),
    ('ict','ICT'),
)

LEVEL_CHOICES = (
	('hsc', 'HSC'),
	('ssc', 'SSC'),

)

YEAR_CHOICES = []
for r in range(2010, (datetime.datetime.now().year+5)):
    YEAR_CHOICES.append((r,r))


def contact_default():
   return {"email": "to1@example.com"}


class TeachersInfo(models.Model):
	name = models.CharField(max_length=100)
	institute = models.CharField(max_length=100)
	subject = models.CharField(max_length=100)
	college = models.CharField(max_length=100)
	hsc_year = models.IntegerField(choices=YEAR_CHOICES, 
						     	   default=datetime.datetime.now().year)

	school = models.CharField(max_length=100)
	ssc_year = models.IntegerField(choices=YEAR_CHOICES, 
								   default=datetime.datetime.now().year)
	date_of_birth = models.DateField(max_length=8, default=timezone.now)

	mentoring_subject = ListCharField(
        base_field = models.CharField(max_length=20),
        size=6,
        max_length=(6 * 21)  # Maximum of 100 ids in list
        #default='Test',
    )
	level = models.CharField(max_length=100, choices=LEVEL_CHOICES, default="hsc")
	deparment = models.CharField(max_length=100,
								choices=DEPARTMENT_CHOICES,
								default="Science")

	summary_of_activites = ListTextField(
        base_field = models.CharField(max_length=100),
        size=100  # Maximum of 100 ids in list
        #default='Test',
    )

	email = models.EmailField(max_length=100)
	address = models.CharField(max_length=255, help_text='Enter your address')
	contact_no = models.CharField(max_length=20, help_text='Enter contact no')
	fb_link = models.CharField(max_length=255, help_text='Enter facebook profile link')
	linkedin_link = models.CharField(max_length=255,help_text='Enter linkedin 	profile link' )
	bio = models.TextField()
	image = models.ImageField(default='default.jpg', upload_to='teachers_pic')
	
	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		img = Image.open(self.image.path)

		if img.height > 418 or img.width > 371:
			#output_size = (418, 371)
			img = img.resize((371, 418), Image.ANTIALIAS)
			# img.thumbnail(output_size)
			img.save(self.image.path)