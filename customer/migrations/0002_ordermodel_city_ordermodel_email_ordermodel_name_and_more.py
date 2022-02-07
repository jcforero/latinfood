# Generated by Django 4.0.2 on 2022-02-06 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='city',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='email',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='state',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='street',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='zip_code',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
