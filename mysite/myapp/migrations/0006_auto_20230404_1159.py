# Generated by Django 3.1.14 on 2023-04-04 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='Comment',
            new_name='comment',
        ),
    ]
