# Generated by Django 4.1.3 on 2022-12-18 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glasses', '0002_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='static/images/glasses/aviator_3.jpg', upload_to=''),
        ),
    ]