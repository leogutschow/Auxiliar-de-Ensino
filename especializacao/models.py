from django.db import models

# Create your models here.

class Especializacao(models.Model):
    especializacao = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.especializacao