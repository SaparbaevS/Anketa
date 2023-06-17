from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    age = models.PositiveIntegerField()

    STATUS = (
        ('st', 'Учусь'),
        ('wk', 'Работаю'),
        ('st', 'Туплю'),
        ('st', 'Мамкин миллиардер'),
        ('st', 'Мамин бродяга, Папин симпотяга'),
    )

    status = models.CharField(max_length=50, choices=STATUS)
    salary = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.surname}"

    def get_absolute_url(self):
        return f"/{self.pk}"
