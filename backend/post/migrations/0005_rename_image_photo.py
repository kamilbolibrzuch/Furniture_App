# Generated by Django 4.0.5 on 2022-06-28 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_remove_post_image_remove_post_thumbnail_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='Photo',
        ),
    ]
