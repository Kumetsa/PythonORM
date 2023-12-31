# Generated by Django 4.2.4 on 2023-11-13 14:07

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import main_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='location',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2, message='Location must be at least 2 characters long.'), django.core.validators.MaxLengthValidator(100, message='Location cannot exceed 200 characters.')]),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2, message='Name must be at least 2 characters long.'), django.core.validators.MaxLengthValidator(100, message='Name cannot exceed 100 characters.')]),
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(validators=[main_app.validators.validate_menu_categories])),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.restaurant')),
            ],
        ),
    ]
