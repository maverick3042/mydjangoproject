from django.db import models

# Create your models here.
class Customer(models.Model):
    image = models.ImageField(upload_to='customer_images/', blank=True)
    name = models.CharField(max_length=20)
    admissionNumber = models.CharField(max_length=10)
    email = models.EmailField(max_length=25)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()

    def __str__(self):
        return self.name