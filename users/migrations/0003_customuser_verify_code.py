# Generated by Django 4.2.4 on 2023-08-19 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='verify_code',
            field=models.CharField(default=None, max_length=4, verbose_name='Код верификации'),
        ),
    ]