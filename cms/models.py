# -*- coding: utf-8 -*-

from django.db import models

class HeartRateData(models.Model):
	pub_date = models.DateTimeField('date published')
	user = models.CharField(max_length=50)

	def __str__(self):
		return str(self.id)

class Content(models.Model):
	heartratedata = models.ForeignKey(HeartRateData, related_name='contents')
	time = models.DateTimeField('date published')
	bpm = models.IntegerField(blank=False, default=0)

	def __str__(self):
		return str(self.bpm)
