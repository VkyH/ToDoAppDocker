from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TodoModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    task=models.CharField(max_length=100,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    # target=models.DateTimeField()
    status=models.BooleanField(default=False)
    
    class Meta:
        ordering = ('status', '-created_at')
        
    def __str__(self):
        return self.task + ' - ' + str(self.status)