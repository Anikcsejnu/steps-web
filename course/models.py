from django.db import models
from django.urls import reverse
from teacher.models import TeachersInfo

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
    
    def __str__(self):
        return self.name
    
    

    
class Chapter(models.Model):
    name_of_course = models.ForeignKey(Course, on_delete = models.CASCADE)
    name_of_chapter = models.CharField(max_length = 100)

    def __str__(self):
        return self.name_of_chapter

    

    
class Topic(models.Model):
    name_of_teacher = models.ManyToManyField(TeachersInfo, blank=True)
    name_of_chapter = models.ForeignKey(Chapter, on_delete = models.CASCADE)
    name_of_topic = models.CharField(max_length = 200)

    def __str__(self):
        return self.name_of_topic
    