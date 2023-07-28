from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    polity = models.DecimalField(max_digits=5, decimal_places=2)
    science_technology = models.DecimalField(max_digits=5, decimal_places=2)
    art_culture = models.DecimalField(max_digits=5, decimal_places=2)
    history = models.DecimalField(max_digits=5, decimal_places=2)
    maths = models.DecimalField(max_digits=5, decimal_places=2)
    reasoning = models.DecimalField(max_digits=5, decimal_places=2)
    ethics = models.DecimalField(max_digits=5, decimal_places=2)
    geography = models.DecimalField(max_digits=5, decimal_places=2)
    literature = models.DecimalField(max_digits=5, decimal_places=2)
    economics = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.name
    
    
