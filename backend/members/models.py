from django.db import models
from django.db.models.functions import Now
from datetime import timedelta
from django.contrib.auth import get_user_model
from django.utils import timezone


User = get_user_model()


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='user_memberObject')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        
        return self.user.get_username() + ' ' + str(self.created_at)

    def get_membership(self):
        
        if hasattr(self,'membership'):
            return self.membership
        
        return None

class WorkoutPlan(models.Model):
    PLANS = (
        ('basic','Basic'),
        ('standard','Standard'),
        ('pro','Pro')
    )
    name = models.CharField(max_length=100, unique=True, primary_key=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name



class Membership(models.Model):
    member = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True,related_name='membership')
    workoutPlan  = models.ForeignKey(WorkoutPlan,on_delete=models.SET_NULL,null=True,related_name='workoutPlan_members')
    start_date = models.DateTimeField(default=timezone.now)
    expiry_date = models.DateTimeField(default=Now()+timedelta(days=30),editable=False)




