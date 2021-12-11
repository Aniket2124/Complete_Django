from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self,email,password=None,is_staff=False,is_active=True,is_admin=False,is_verified=False,is_teacher=True):
        if not email:
            raise ValueError("User must have an Email address")
        if not password:
            raise ValueError("User must have Password")
        user_obj = self.model(email=self.normalize_email(email))
        user_obj.set_password(password)
        user_obj.is_active = is_active
        user_obj.is_staff = is_staff
        user_obj.is_admin = is_admin
        user_obj.save(using=self._db)
        return user_obj


    def create_staffuser(self,email,password=None):
        user = self.create_user(email, password=password,is_staff=True,is_verified=True,is_teacher=False)
        return user
    def create_superuser(self,email,password=None):
        user = self.create_user(email, password=password,is_admin=True,is_staff=True,is_verified=True,is_teacher=False)
        return user




class User(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'  # this now over rides the username field and now email is the default field
    # REQUIRED_FIELDS = [] if you add another field and need it to be required, include it in the listh

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    # @property
    # def is_staff(self):
    #     return self.staff

    # @property
    # def is_admin(self):
    #     return self.admin
