# Generated by Django 4.2 on 2023-04-28 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_options_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
