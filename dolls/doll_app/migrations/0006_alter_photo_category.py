# Generated by Django 4.1.1 on 2022-09-18 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doll_app', '0005_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='category',
            field=models.ForeignKey(choices=[('Феечка', 'Феечка'), ('Лисичка', 'Лисичка'), ('Санта', 'Санта')], on_delete=django.db.models.deletion.CASCADE, to='doll_app.dolls'),
        ),
    ]