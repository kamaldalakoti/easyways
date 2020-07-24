from django.db import models

# Create your models here.
class Hospital(models.Model):
    Name = models.CharField(max_length=20)
    Doctor = models.CharField(max_length=30)
    Doctor_of = models.TextField(max_length=110  )
    Contact = models.TextField(max_length=110  )
    Timing = models.TextField(max_length=110  )
    Location = models.TextField(max_length=110  )
    pictures = models.FileField(upload_to="static", storage=None)
    def __str__(self):
        return self.Name      

class Shop(models.Model):
    Shop_name = models.CharField(max_length=20)
    Area = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    State = models.CharField(max_length=20)
    Product_name = models.CharField(max_length=20)
    Phone_no = models.CharField(max_length=20)
    Shop_discription = models.CharField(max_length=200)
    Pic_shop = models.FileField(upload_to="static", storage=None)
    pic_product = models.FileField(upload_to="static", storage=None)
    def __str__(self):
        return self.Shop_name

class Tour(models.Model):
    Name_tour = models.CharField(max_length=20)

    Pic_tour = models.FileField(upload_to="static", storage=None)
