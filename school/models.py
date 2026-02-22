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
        return f"{self.last_name} {self.first_name}"

class SchoolClass(models.Model):
    name = models.CharField(max_length=10, verbose_name="Назва класу")
    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.last_name} {self.first_name}"

class Timetable(models.Model):
    DAYS = [('ПН', 'Пн'), ('ВТ', 'Вт'), ('СР', 'Ср'), ('ЧТ', 'Чт'), ('ПТ', 'Пт')]
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
    subject = models.ForeignKey(Uroks, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    day = models.CharField(max_length=2, choices=DAYS)
    lesson_number = models.PositiveIntegerField()

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    urok = models.ForeignKey(Uroks, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)