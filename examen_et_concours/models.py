from django.db import models
from PIL import Image

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Solution(models.Model):
    title = models.CharField('Nom',max_length=100)
    solution_file = models.FileField(upload_to='solutions')
    price = models.CharField(max_length=30)
    creator = models.CharField(max_length=30)

    
    def __str__(self):
        return self.title

class Matter(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Level(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Etablissement(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Year(models.Model):
    year = models.DateField(blank=True,null=True)
    
    def __str__(self):
        return str(self.year.year)
   

class Concours(models.Model):
    name = models.CharField('Nom',max_length=100)
    description = models.TextField('Description')
    image = models.ImageField(upload_to='image/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height >100 or img.width>100:
            output_size = (200,200)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Subject(models.Model):
   
    title = models.CharField('Nom',max_length=100, default='Aucun')
    subject_file = models.FileField(upload_to='sujects', blank=True,null=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, blank=True,null=True)
    matter = models.ForeignKey(Matter, on_delete=models.CASCADE, blank=True,null=True)
    etablissement = models.ForeignKey(Etablissement, on_delete=models.CASCADE, blank=True,null=True)
    year = models.ForeignKey(Year, on_delete=models.CASCADE,default=2014)
    examen = models.ForeignKey(Concours, on_delete=models.CASCADE, blank=True,null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank= True,null= True)
    solution = models.OneToOneField(Solution, on_delete=models.CASCADE, blank=True,null=True)

    
    def __str__(self):
        return self.title




