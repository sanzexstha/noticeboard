# Generated by Django 3.0.4 on 2020-03-10 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20200310_0814'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='commented_by',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='posted_by',
        ),
    ]