from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Custom User Manager
class AccountManager(BaseUserManager):
    def create_user(self,email,username,fullname,gender,password=None):
        if not email:
            raise ValueError('Enter a valid email.')
        if not username:
            raise ValueError('Enter username.')
        if not fullname:
            raise ValueError('Enter you name.')
        if not gender:
            raise ValueError('Enter you gender.')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            fullname=fullname,
            gender=gender,
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self,email,username,fullname,gender,password):
        user = self.create_user(
            username=username,
            email=self.normalize_email(email),
            fullname=fullname,
            gender=gender,
            password=password,
        )
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self.db)
        return user


#Custom User Model
class Account(AbstractBaseUser):
    fullname = models.CharField(verbose_name='Name', max_length=30)
    username = models.CharField(verbose_name='Username',max_length=20,unique=True)
    email = models.EmailField(verbose_name='Email', unique=True)
    gender = models.CharField(verbose_name='Gender', max_length=12)
    contact = models.CharField(verbose_name='Contact', max_length=14)
    location = models.CharField(verbose_name='Address', max_length= 50)
    date_joined = models.DateTimeField(verbose_name='Join date', auto_now_add=True)
    is_banned = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['fullname','email','gender']
    objects = AccountManager()

    def __Str__(self):
        return self.username

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True


class Profile(models.Model):
    user = models.OneToOneField(Account,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_photos')

    def __str__(self):
        return self.user.username