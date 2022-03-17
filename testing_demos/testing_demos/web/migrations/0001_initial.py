# Generated by Django 4.0.3 on 2022-03-17 18:03

import django.core.validators
from django.db import migrations, models
import testing_demos.common.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25, validators=[testing_demos.common.validators.validate_only_letters])),
                ('last_name', models.CharField(max_length=25, validators=[testing_demos.common.validators.validate_only_letters])),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(150)])),
            ],
        ),
    ]