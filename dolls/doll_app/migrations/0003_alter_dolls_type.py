# Generated by Django 4.1.1 on 2022-09-17 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doll_app', '0002_alter_dolls_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dolls',
            name='type',
            field=models.CharField(choices=[('Интерьерная кукла', 'Интерьерная кукла'), ('G', 'Игровая кукла'), ('D', 'Игрушка'), ('A', 'Одежда для куклы'), ('B', 'Одежда для игрушки')], max_length=30),
        ),
    ]
