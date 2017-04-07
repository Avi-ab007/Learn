from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	BRANCH = (
		('CSE', 'CSE'),
		('MECH', 'MECH'),
		('ECE', 'ECE'),
		('EEE', 'EEE'),
		('CIVIL', 'CIVIL'),
		('META', 'META'),
		)
	department = models.CharField(max_length=5, choices=BRANCH)
	picture = models.ImageField(upload_to='profile_pictures', default='default_pic.jpg')
	isAdmin = models.BooleanField(default=False)

	def __str__(self):
		return self.user.username
