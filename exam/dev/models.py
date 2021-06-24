from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.name

class Question(models.Model):
    category = models.ForeignKey(Category,on_delete=models.RESTRICT)
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.name
    
class Option(models.Model):
    question = models.ForeignKey(Question,on_delete=models.RESTRICT)
    name = models.CharField(max_length=200)
    points = models.IntegerField()
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.name