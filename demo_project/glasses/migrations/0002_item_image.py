# Generated by Django 4.1.3 on 2022-12-18 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glasses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(default='static/images/glass1.png', upload_to=''),
        ),
    ]
