# Generated by Django 3.1.3 on 2020-11-18 18:14

import Models.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0011_remove_facedetection_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facedetection',
            name='picture',
            field=models.ImageField(upload_to='submitted_pictures', validators=[Models.models.validate_pic_type]),
        ),
    ]