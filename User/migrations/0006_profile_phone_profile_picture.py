# Generated by Django 4.2.6 on 2023-11-08 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_alter_profile_age_alter_profile_initial_biceps_size_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, default='user-default.png', null=True, upload_to=''),
        ),
    ]
