# Generated by Django 5.0.3 on 2024-03-28 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]