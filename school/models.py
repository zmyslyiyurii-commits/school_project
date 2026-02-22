from django.db import models

class Uroks(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    urok = models.ForeignKey(Uroks, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.last_name} {self.first_name}"

class SchoolClass(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name

# ОСЬ ЦЬОГО БРАКУВАЛО:
class Timetable(models.Model):
    DAYS_OF_WEEK = [
        ('ПН', 'Понеділок'),
        ('ВТ', 'Вівторок'),
        ('СР', 'Середа'),
        ('ЧТ', 'Четвер'),
        ('ПТ', "П'ятниця"),
    ]

    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
    subject = models.ForeignKey(Uroks, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    day = models.CharField(max_length=2, choices=DAYS_OF_WEEK)
    lesson_number = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.school_class} - {self.day} - {self.lesson_number}"