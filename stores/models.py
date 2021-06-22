from django.db import models

# Create your models here.

class Pizzeria(models.Model):
    pizzeria_name=models.CharField(max_length=255,blank=False)
    street=models.CharField(max_length=400,blank=False)
    state=models.CharField(max_length=2,null=True,blank=True)
    zip_code=models.IntegerField(blank=True,default=0)
    website=models.URLField(max_length=420,null=True)
    logo_image=models.ImageField(upload_to='pizzaimages',
        default='pizzaimages/default.jpg',blank=True)

    email=models.EmailField(max_length=255,blank=True)
    active=models.BooleanField(default=True)


    def __str__(self):
        return f"{self.pizzeria_name} in {self.state}"

