# Generated by Django 2.1.3 on 2018-12-23 11:52

from django.db import migrations, models
import music_publisher.base


class Migration(migrations.Migration):

    dependencies = [
        ('music_publisher', '0015_auto_20181201_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='original_title',
            field=models.CharField(blank=True, db_index=True, max_length=60, validators=[music_publisher.base.CWRFieldValidator('work_title')]),
        ),
    ]
