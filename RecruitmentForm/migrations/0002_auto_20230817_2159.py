# Generated by Django 3.2.19 on 2023-08-17 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecruitmentForm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrations',
            name='mobile',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='registrations',
            name='whatsappnumber',
            field=models.IntegerField(),
        ),
    ]