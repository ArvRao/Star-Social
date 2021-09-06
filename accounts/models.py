from django.db import models
from django.contrib import auth
# Create your models here.

class User(auth.models.User, auth.models.PermissionsMixin):
    #User used to generate a form for signing up and logging in
    #PermissionsMixin used for customizing auth
    ''' To make it easy to include Django’s permission framework into your own user class,
    Django provides PermissionsMixin.
    This abstract model included in class hierarchy w/ user model.
    '''
    def __str__(self):
        return '@{}'.format(self.username)