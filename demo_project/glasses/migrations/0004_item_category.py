# Generated by Django 4.1.3 on 2022-12-19 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glasses', '0003_alter_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('Glasses', 'Glasses')], default='G', max_length=7),
            preserve_default=False,
        ),
    ]
