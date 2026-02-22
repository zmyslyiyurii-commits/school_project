from django.db import models

class Uroks(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва предмета")

    def __str__(self):
        return self.name

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    urok = models.ForeignKey(Uroks, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"