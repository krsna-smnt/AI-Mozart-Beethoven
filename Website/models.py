# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class Music(models.Model):
	audio = models.FileField(upload_to='media/')
	upload_dt = models.DateField(default=timezone.now)

	def __str__(self):
		return str(self.pk)