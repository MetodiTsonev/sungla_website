# Generated by Django 4.1.3 on 2022-11-25 09:25

import demo_project.accounts.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_appuser_age_alter_appuser_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(150)]),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='first_name',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), demo_project.accounts.models.validate_only_letters]),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('Other', 'Other')], max_length=6),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='last_name',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), demo_project.accounts.models.validate_only_letters]),
        ),
    ]