# Generated by Django 2.1.4 on 2019-01-21 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_publisher', '0021_remove_cwrexport__work_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='cwrexport',
            name='description',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]
