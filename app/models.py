from operator import mod
from pyexpat import model
from django.conf import settings
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin



class UserAccountManager(BaseUserManager):

    def create_user(self,username ,email, location=None,state=None,gender=None, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError("User must have an username")

        email = self.normalize_email(email)
        email = email.lower()

        user = self.model(
            username=username,
            email=email,
            location=location,
            state=state,
            gender=gender
            )

        
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,username,email,password=None):
        user = self.create_user(
            username = username,
            email = email,
            password=password)

        user.is_staff =True
        user.is_superuser = True
        user.save(using = self._db)

        return user
  



class UserAccount(AbstractBaseUser, PermissionsMixin):

    username =   models.CharField(max_length=50 , unique=True)
    email = models.EmailField( max_length=255)
    location = models.CharField(max_length=50,null= True)
    state = models.CharField(max_length=50,null= True)
    gender = models.CharField(max_length=50,null= True)
    is_staff = models.BooleanField(default=False)
    

    objects = UserAccountManager()

    USERNAME_FIELD = 'username'
    
    REQUIRED_FIELDS = ['email']

    

    def __str__(self):
        return self.username


class Post(models.Model):
    image = models.ImageField(upload_to='images')
    user = models.ForeignKey(UserAccount,on_delete=models.CASCADE )
    description = models.CharField(max_length= 200 ,null = True)