from django.db import models

# Create your models here.
class Call_Tokens(models.Model):
    tokens = models.PositiveBigIntegerField()
    call_status = models.BooleanField(default=False)
    captions = models.CharField(max_length=255,null=True,blank=True)
    generate_time = models.DateTimeField(auto_now_add=True)
    call_time = models.DateTimeField(auto_now_add=False,null=True,blank=True) 
    
    def __str__(self):
        return str(self.tokens)
