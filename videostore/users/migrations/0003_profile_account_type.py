# Generated by Django 4.1.7 on 2023-03-02 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_options_alter_profile_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='account_type',
            field=models.CharField(choices=[('full', 'Полный пакет'), ('free', 'Бесплатный пакет')], default='free', max_length=30),
        ),
    ]
