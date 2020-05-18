from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
	"""Manager for user profile"""

	def create_user(self, email, name, password=None):
		if not email:
			raise ValueError('User need to have email')
		email = self.normalize_email(email)

		# Create an instance of UserProfile
		user = self.model(email=email, name=name)
		user.set_password(password)

		# Save to DB
		user.save(using=self._db)

		return user

	def create_superuser(self, email, name, password):
		"""Create and save a superuser with given detail"""
		user = self.create_user(email, name, password)

		# Set up some detail
		user.is_superuser = True
		user.is_staff = True

		# Save to DB
		user.save(using=self._db)

		return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
	"""Database model for user in the system"""
	email = models.EmailField(max_length=255, unique=True)
	name = models.CharField(max_length=255)

	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	# Custom model manager for user model
	objects = UserProfileManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['name']

	def get_full_name(self):
		return self.name

	def __str__(self):
		return self.email

