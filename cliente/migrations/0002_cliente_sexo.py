# Generated by Django 4.2.4 on 2023-08-09 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='sexo',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('N', 'Nullo')], default='N', max_length=1),
        ),
    ]
