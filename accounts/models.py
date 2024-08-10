from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True, null=False)
    username = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# class CustomeUserManage(BaseUserManager):
#     def create_user(self, email, phone, name, password):
#         if not email and not phone and not name and not password:
#             raise ValueError('email, phone, name and password should not be empty')
        
#         user = self.model(
#             email = self.normalize_email(email),
#             phone = phone,
#             name = name,
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user
    


# class CustomUser(AbstractBaseUser):
#     email = models.EmailField(max_length=255, unique=True, blank=True, null=True)
#     phone = models.CharField(max_length=15, unique=True, blank=True, null=True)
#     name = models.CharField(max_length=255)
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)

#     objects = CustomeUserManage()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['phone', 'name']

#     def __str__(self):
#         return self.email if self.email else self.phone

#     def has_perm(self, perm, obj=None):
#         return True

#     def has_module_perms(self, app_label):
#         return True

#     @property
#     def is_staff(self):
#         return self.is_admin


