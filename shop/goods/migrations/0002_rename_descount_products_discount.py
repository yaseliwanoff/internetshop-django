# Generated by Django 4.2 on 2024-04-07 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='descount',
            new_name='discount',
        ),
    ]