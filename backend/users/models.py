from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):    
    phone_number = models.CharField(max_length=11,unique=True)

    def get_member(self):
        try:
            return self.user_memberObject
        except AttributeError:
            return None
        except Exception as e:
            
            print(e)
            
            return None
