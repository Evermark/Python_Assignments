from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class UserManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first name"] = "First name must be more than 2 characters."
        if len(postData['last_name']) < 2:
            errors["last name"] = "Last name must be more than 2 characters."
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Must provide valid email address."
        if len(postData['password']) < 8 :
            errors["password"] = "Passowrd must contain 8 characters."
        if postData['password'] != postData['confirm_pw']:
            errors["password"] = "Passwords must match."
        return errors

    def pw_hasher(self, pwd):
        Password = bcrypt.hashpw(pwd.encode(),bcrypt.gensalt())
        return Password

    def login_validator(self, postData):
        errors = {}
        for key in postData:
            if postData['key'] == "":
                errors["empty_field"] = "please input email and password."
            return errors

        #Find User in DB
        this_user = User.objects.filter(Email=postData['Email'])

        #try to check DB for User Info
        try:
            if not bcrypt.checkpw(postData['password'].encode(), this_user[0].encode()):
                errors['login_fail'] = "Input does not match our database. Register or try again."
        except:
            errors['login_fail'] = "Input does not match our database. Register or try again."
            return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()
