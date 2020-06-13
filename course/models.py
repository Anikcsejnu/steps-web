from django.db import models
from django.urls import reverse
from teacher.models import *
from django.utils import timezone

# Create your models here.

DEPARTMENT_CHOICES = (
    ('SCIENCE','Science'),
    ('BUSINESS STUDIES', 'Business Studies'),
    ('ENGLISH', 'English'),
    ('ICT','Ict'),
)

LEVEL_CHOICES = (
	('HSC', 'HSC'),
	('SSC', 'SSC'),

)

class Course(models.Model):
    name = models.CharField(max_length = 200)
    short_details = models.CharField(max_length = 1000)
    dept = models.CharField(max_length = 100, choices = DEPARTMENT_CHOICES, default = 'Science')
    level = models.CharField(max_length = 100, choices = LEVEL_CHOICES, default = 'HSC')
    background = models.ImageField( default = 'course_background/default.jpg', upload_to='course_background')
    thumbnail = models.ImageField( default = 'course_thumbnail/default.jpg', upload_to='course_thumbnail')
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
	    super().save(*args, **kwargs)

	    img = Image.open(self.thumbnail.path)

	    if img.height > 523 or img.width > 228:
		    img = img.resize((523, 228), Image.ANTIALIAS)
		    img.save(self.thumbnail.path)
    
    

    
class Chapter(models.Model):
    name_of_course = models.ForeignKey(Course, on_delete = models.CASCADE)
    name_of_chapter = models.CharField(max_length = 100)

    def __str__(self):
        return self.name_of_chapter
    

    

    
class Topic(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete = models.CASCADE, default = '') 
    name_of_topic = models.CharField(max_length = 200)

    def __str__(self):
        return self.name_of_topic


class Tutorial(models.Model):

    name_of_topic = models.ForeignKey(Topic, on_delete = models.CASCADE, default = '')
    name_of_teacher = models.ForeignKey(TeachersInfo, related_name='tutorials', on_delete = models.CASCADE)
    uploaded_time = models.DateTimeField(default=timezone.now())
    video_link = models.CharField(max_length=400, default = "")
    file_link = models.CharField(max_length=400, default=" ")


    
