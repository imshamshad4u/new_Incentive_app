from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class employee(models.Model):
    # EmpId = models.AutoField(primary_key=True)
    # user = models.ForeignKey(
    #     User, on_delete=models.CASCADE, null=True, blank=True)
    EmpName = models.CharField(max_length=200)
    EmpEmail = models.CharField(max_length=200)
    EmpPass = models.CharField(max_length=100, default="")
    EmpDepartment = models.CharField(max_length=50, choices=(
        ('IT', 'IT'), ('HR', 'HR'), ('Accounts', 'Accounts'), ('Finance', 'Fianace')))
    EmpDescription = models.TextField()
    EmpFile = models.FileField(upload_to='media')

    def __str__(self):
        return self.EmpName+" depatment is: "+self.EmpDepartment

# class userdetails(models.Model):
