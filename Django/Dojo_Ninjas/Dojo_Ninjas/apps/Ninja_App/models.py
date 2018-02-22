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

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo = models.ForeignKey(Dojo, related_name = 'ninjas')
