# Generated by Django 2.2.3 on 2019-11-17 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hedgehog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hedgehog',
            name='image',
            field=models.ImageField(null=True, upload_to='myapp'),
        ),
    ]
