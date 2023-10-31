from django.db import models

# Create your models here.
class contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    phone =models.CharField(max_length=13)
    email = models.EmailField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True , blank=True)


    def __str__(self) -> str:
        return 'Message From '+ self.name