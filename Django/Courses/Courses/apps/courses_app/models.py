from __future__ import unicode_literals
from django.db import models

class Validator(models.Manager):
    def course_validator(self, postData):
        errors = {}
        if len(postData['course_name']) < 5:
            errors['course_name'] = "Course Name must be more than 5 characters."
        if len(postData['desc']) < 15:
            errors['desc'] = "Course Description must be more than 15 characters."
        return errors

class Course(models.Model):
    course_name = models.CharField(max_length=255)
    desc = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    objects = Validator()
