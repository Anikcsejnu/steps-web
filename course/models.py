from django.db import models
from django.urls import reverse
from teacher.models import *
from django.utils import timezone
from smart_selects.db_fields import ChainedForeignKey

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
        return '{}{}{}'.format(self.level, '_', self.name)
    
    

    
class Chapter(models.Model):
    name_of_course = models.ForeignKey(Course, on_delete = models.CASCADE)
    name_of_chapter = models.CharField(max_length = 100)

    def __str__(self):
        return self.name_of_chapter

    

    
class Topic(models.Model):
    course_name = models.ForeignKey(Course, on_delete = models.CASCADE, default='')
    chapter = ChainedForeignKey(Chapter, 
                                chained_field="course_name", 
                                chained_model_field="name_of_course",
                                show_all=False,
                                auto_choose=True,
                                default='',
                                ) 
    name_of_topic = models.CharField(max_length = 200)

    def __str__(self):
        return self.name_of_topic

class Tutorial(models.Model):

    course_name = models.ForeignKey(Course, on_delete = models.CASCADE)
    chapter = ChainedForeignKey(Chapter, 
                                chained_field="course_name", 
                                chained_model_field="name_of_course",
                                show_all=False,
                                auto_choose=True,
                                default='',
                                ) 
    name_of_topic = ChainedForeignKey(Topic, 
                                chained_field="chapter", 
                                chained_model_field="chapter",
                                show_all=False,
                                auto_choose=True,
                                default='',
                                )
    name_of_teacher = models.ForeignKey(TeachersInfo, on_delete = models.CASCADE)
    uploaded_time = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return '{}{}{}{}{}{}{}'.format(self.course_name, 'by',
                                   self.chapter, '_',
                                   self.name_of_topic, '_',
                                   self.name_of_teacher)

