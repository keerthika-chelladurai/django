from django.db import models

# Create your models here.

class student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    course = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
# Create the database table

# python manage.py makemigrations
# python manage.py migrate
# python manage.py showmigrations
# [X] 0001_initial -the [x] means the migration has been applied.
# if want to updated the model structure, add the new field in model and create above migration codes again in terminal.

"""
models.py
   ⇩
makemigrations
   ⇩
migration file
   ⇩
migrate
   ⇩
database table
         
"""
