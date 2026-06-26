from django.db import models

# Create your models here.
class departments(models.Model):
    dept_name = models.CharField(max_length=100)
    dep_description = models.TextField()

class doctors(models.Model):
    doc_name = models.CharField(max_length=100)
    doc_spec = models.CharField(max_length=100)
    dep_name = models.ForeignKey(departments,on_delete=models.CASCADE)

    doc_image = models.ImageField(upload_to='doctors')

class booking(models.Model):
    p_name = models.CharField(max_length=100)
    p_phone = models.CharField(max_length=15)
    p_email = models.EmailField()
    doc_name = models.ForeignKey(doctors, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now_add=True)
