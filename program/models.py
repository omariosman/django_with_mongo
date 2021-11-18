from django.db import models

# Create your models here.


class Program(models.Model):
    name = models.CharField(max_length=50)

class Instruction(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    type = models.CharField(max_length=10)
    var = models.CharField(max_length=10)
    inst = models.CharField(max_length=300)



