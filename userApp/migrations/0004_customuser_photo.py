# Generated by Django 3.0.5 on 2021-05-05 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0003_remove_customuser_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='prifilePics/'),
        ),
    ]
