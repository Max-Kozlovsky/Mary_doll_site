from django.db import models


class Dolls(models.Model):
    type_choice = (
        ('Интерьерные куколки', "Интерьерная кукла"),
        ('Игровые куколки', "Игровая кукла"),
        ('Игрушки', "Игрушка"),
        ('Одежда для кукол', "Одежда для куклы"),
        ("Одежда для игрушек", "Одежда для игрушки")
    )
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=30, choices=type_choice)
    available = models.CharField(max_length=30)
    description = models.TextField()
    price = models.IntegerField()
    image = models.FileField(upload_to='static/img/')

    def __str__(self):
        return self.name


class Photo(models.Model):
    dolls = models.ForeignKey(Dolls, on_delete=models.CASCADE, null=True)
    img = models.FileField(upload_to='static/photo/')

    def __str__(self):
        return self.dolls.name
