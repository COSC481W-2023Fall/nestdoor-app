from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager
# Create your models here.

class React(models.Model):
    name = models.CharField(max_length=30)
    detail = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.name} {self.detail}"
      

class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    addr = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# # #Custom Account Manager for Griffin's testing...
# class MyAccountManager(BaseUserManager):
#     def create_user(self, email, username, password=None):
#         if not email:
#             raise ValueError("Users must have an email address.")
#         if not username:
#             raise ValueError("Users must have an username.")

#         user = self.model(
#             email=self.normalize_email(email),
#             username=username,
#             )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, username, password):
#         user = self.create_user(
#             email=self.normalize_email(email),
#             password=password,
#             username=username,
#         )

#         user.is_admin = True
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user

# # #Custom User Class for Griffin's testing...
# class Account(AbstractBaseUser):
#     email                   = models.EmailField(verbose_name="email", max_length=60, unique=True)
#     username                = models.CharField(max_length=30, unique=True)
#     date_joined             = models.DateTimeField(verbose_name='date_joined', auto_now_add=True)
#     last_login              = models.DateTimeField(verbose_name='last_login', auto_now=True)
#     is_admin                = models.BooleanField(default=False)
#     is_active               = models.BooleanField(default=False)
#     is_staff                = models.BooleanField(default=False)
#     is_superuser            = models.BooleanField(default=False)
    
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['username']

#     objects = MyAccountManager()

#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         return self.is_admin

#     def has_module_perms(self, app_label):
#         return True