from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from django.conf import settings


class MyAccountManager(BaseUserManager):
    """
    Class of Manager Account
    """
    def create_user(self, username, password, is_staff=False, is_admin=False, is_superuser=False, **kwargs):
        """Method to create a user"""
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(username=username)
        user.set_password(password)
        user.is_admin = is_admin
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save(using=self._db)
        return user

    def create_staffuser(self, username, password=None):
        """Method to create a staff user"""
        if not username:
            raise ValueError('Staff Users must have an username')
        user = self.create_user(username=username, password=password, is_staff=True)
        return user

    def create_superuser(self, username, password=None):
        """Method to create a super user"""
        if not username:
            raise ValueError('Super Users must have an username')
        user = self.create_user(username=username, password=password, is_admin=True, is_superuser=True, is_staff=True)
        return user


class Account(AbstractBaseUser):
    """
    Class of Account
    """
    username = models.CharField(verbose_name='username', max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = MyAccountManager()

    def __str__(self):
        """Get username by default"""
        return self.username

    def has_perm(self, perm, obj=None):
        """Check if has admin permission"""
        return self.is_admin

    def has_module_perms(self, app_label):
        """Check if has module permission"""
        return True


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
