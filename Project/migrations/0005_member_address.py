# Generated by Django 4.2.6 on 2023-11-08 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0004_member_mobile_number_alter_member_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
