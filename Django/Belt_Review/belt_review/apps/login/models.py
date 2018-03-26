from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        try:
            if User.objects.get(email=postDate['email']):
                errors['registration error'] = "User already exists. Please login."
        except:
            pass
        if len(postData['name']) < 4:
            errors["name"] = "Name must be more than 4 characters."
        if len(postData['alias']) < 4:
            errors["alias"] = "Alias must be more than 4 characters."
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Must provide valid email address."
        if len(postData['password']) < 8 :
            errors["password"] = "Passowrd must contain 8 characters."
        if postData['password'] != postData['confirm_pw']:
            errors["password"] = "Passwords must match."
        return errors

    def pw_hasher(self, pwd):
        password = bcrypt.hashpw(pwd.encode(),bcrypt.gensalt())
        return Password

    def login_validator(self, postData):
        errors = {}
        if postData['email'] == "":
            errors["empty email"] = "Please enter email address."
        if postData['password'] == "":
            errors["empty password"] = "Please enter password."
        return errors

        #Find current user in DB
        this_user = User.objects.filter(email=postData['email'])

class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()
