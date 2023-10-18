from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class StudentManager(BaseUserManager):
    def create_user(self, studentname, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), studentname=studentname)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, studentname, email, password=None):
        user = self.create_user(studentname, email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Student(AbstractBaseUser, PermissionsMixin):
    studentname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = StudentManager()  

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['studentname']

    def __str__(self):
        return self.email
