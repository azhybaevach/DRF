from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=123)
    last_name = models.CharField(max_length=123)
    birth_of_date = models.DateField()
    hobby = models.CharField(max_length=132)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    disciplines = models.ManyToManyField('Discipline', blank=True, null=True)

    def __str__(self):
        return f'{self.first_name}'


class Discipline(models.Model):
    title = models.CharField(max_length=123)
    description = models.CharField(max_length=123)
    start_date = models.TimeField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'



