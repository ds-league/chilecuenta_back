from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                       PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and save a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that suppors using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Family(models.Model):
    index        = models.IntegerField()
    index_exp    = models.IntegerField()
    folio        = models.CharField(max_length=255)
    ingreso      = models.FloatField()
    fe           = models.IntegerField()
    np           = models.IntegerField()
    gasto        = models.FloatField()
    ingreso_disp = models.FloatField()
    ptge_gasto   = models.FloatField()


class Expense(models.Model):
    g            = models.CharField(max_length=255)
    c1           = models.FloatField()
    c2           = models.FloatField()
    c3           = models.FloatField()
    c4           = models.FloatField()
    c5           = models.FloatField()
    c6           = models.FloatField()
    c7           = models.FloatField()
    c8           = models.FloatField()
    c9           = models.FloatField()
    c10          = models.FloatField()
    c11          = models.FloatField()
    c12          = models.FloatField()
    ahorro_deuda = models.FloatField()
    ingreso      = models.FloatField() #ing_disp_hog_hd_pc


class People(models.Model):
    folio       = models.CharField(max_length=255)
    inga_hd     = models.FloatField()
    fe          = models.FloatField()
    persona     = models.FloatField()
    npersonas   = models.FloatField()
    edad        = models.FloatField()
    ingreso_hd  = models.FloatField()
    ingreso_pc  = models.FloatField()
