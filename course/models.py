from django.db import models
from django.urls import reverse

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

class course(models.Model):
    name = models.CharField(max_length = 200)
    short_details = models.CharField(max_length = 1000)
    dept = models.CharField(max_length = 100, choices = DEPARTMENT_CHOICES, default = 'Science')
    level = models.CharField(max_length = 100, choices = LEVEL_CHOICES, default = 'HSC')
    
    def __str__(self):
        return self.name
    
    

    
class chapterlist(models.Model):
    nameOfCourse = models.ForeignKey(course, on_delete = models.CASCADE)
    nameOfChapters = models.CharField(max_length = 100)

    def __str__(self):
        return self.nameOfChapters

    

    
