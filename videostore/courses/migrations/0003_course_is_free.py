# Generated by Django 4.1.7 on 2023-03-02 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_lesson'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_free',
            field=models.BooleanField(default=True, verbose_name='Бесплатно?'),
        ),
    ]