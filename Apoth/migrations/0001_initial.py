# Generated by Django 4.1.7 on 2023-03-17 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('sname', models.CharField(max_length=1000)),
                ('property', models.CharField(max_length=1000)),
                ('location', models.CharField(max_length=1000)),
            ],
        ),
    ]
