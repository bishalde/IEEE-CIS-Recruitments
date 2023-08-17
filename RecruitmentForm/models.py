from django.db import models


class Registrations(models.Model):
    RegistrationId = models.AutoField(primary_key=True)
    fullname=models.CharField(max_length=100)
    registrationNumber=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    section=models.CharField(max_length=100)
    srmmail=models.EmailField(max_length=100)
    personalmail=models.EmailField(max_length=100)
    mobile=models.IntegerField()
    whatsappnumber=models.IntegerField()
    year=models.IntegerField(1)
    domain1=models.CharField(max_length=100)
    domain2=models.CharField(max_length=100)
    linkedin=models.URLField(max_length=300)
    github=models.URLField(max_length=300)
    resume=models.URLField(max_length=300)
    question1=models.TextField(max_length=1000)
    question2=models.TextField(max_length=1000)


    def __str__(self):
        return self.fullname+' - '+self.registrationNumber