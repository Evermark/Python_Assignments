from __future__ import unicode_literals
from django.db import models

# Dojo
# Have it include the name of the dojo and the city and state of each dojo
# Have the first dojo be "CodingDojo Silicon Valley" in "Mountain View", "CA".
# Have the second dojo be "CodingDojo Seattle" in "Seattle", "WA".
# Have the third dojo be "CodingDojo New York" in "New York", "NY".
# Ninja
# Have it include first_name, last_name of each ninja in the dojo.
# Each dojo can have multiple ninjas and each ninja belongs to a specific dojo.

# Using Django Shell:
# Create 3 dojos
# Delete the three dojos you created (e.g. Dojo.objects.get(id=1).delete())
# Create 3 additional dojos by using Dojo.objects.create
# Create 3 ninjas that belong to the first dojo you created.
# Create 3 more ninjas and have them belong to the second dojo you created.
# Create 3 more ninjas and have them belong to the third dojo you created.
# Be able to retrieve all ninjas that belong to the first Dojo
# Be able to retrieve all ninjas that belong to the last Dojo

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo = models.ForeignKey(Dojo, related_name = 'ninjas')
