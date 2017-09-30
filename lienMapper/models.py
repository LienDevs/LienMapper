# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Property(models.Model):
	code = models.CharField(max_length=200)
	owner = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	state = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	bid = models.IntegerField(default=0)
	date = models.DateTimeField()
	lat = models.FloatField()
	lng = models.FloatField()

	