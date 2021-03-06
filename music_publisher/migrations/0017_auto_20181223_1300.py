# Generated by Django 2.1.3 on 2018-12-23 13:00

from django.db import migrations, models
import music_publisher.base


class Migration(migrations.Migration):

    dependencies = [
        ('music_publisher', '0016_work_original_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='albumcd',
            name='_cwr',
        ),
        migrations.RemoveField(
            model_name='alternatetitle',
            name='_cwr',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='_cwr',
        ),
        migrations.RemoveField(
            model_name='firstrecording',
            name='_cwr',
        ),
        migrations.RemoveField(
            model_name='work',
            name='_cwr',
        ),
        migrations.RemoveField(
            model_name='writer',
            name='_cwr',
        ),
        migrations.AlterField(
            model_name='albumcd',
            name='cd_identifier',
            field=models.CharField(blank=True, help_text='This will set the purpose to Library.', max_length=15, null=True, unique=True, validators=[music_publisher.base.CWRFieldValidator('cd_identifier')], verbose_name='CD identifier'),
        ),
        migrations.AlterField(
            model_name='work',
            name='original_title',
            field=models.CharField(blank=True, db_index=True, help_text='Use only for modification of existing works.', max_length=60, validators=[music_publisher.base.CWRFieldValidator('work_title')]),
        ),
        migrations.AlterField(
            model_name='writer',
            name='generally_controlled',
            field=models.BooleanField(default=False, verbose_name='General agreement'),
        ),
        migrations.AlterField(
            model_name='writer',
            name='pr_society',
            field=models.CharField(blank=True, choices=[('055', 'SABAM, Belgium'), ('101', 'SOCAN, Canada'), ('088', 'CMRRA, Canada'), ('040', 'KODA, Denmark'), ('089', 'TEOSTO, Finland'), ('058', 'SACEM, France'), ('035', 'GEMA, Germany'), ('074', 'SIAE, Italy'), ('023', 'BUMA, Netherlands'), ('078', 'STEMRA, Netherlands'), ('090', 'TONO, Norway'), ('079', 'STIM, Sweden'), ('052', 'PRS, United Kingdom'), ('044', 'MCPS, United Kingdom'), ('010', 'ASCAP, United States'), ('021', 'BMI, United States'), ('071', 'SESAC Inc., United States'), ('034', 'HFA, United States'), ('319', 'ICE Services, Administrative Agency'), ('707', 'Musicmark, Administrative Agency')], max_length=3, null=True, validators=[music_publisher.base.CWRFieldValidator('writer_pr_society')], verbose_name='Performing rights society'),
        ),
    ]
