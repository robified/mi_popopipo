# Generated by Django 2.2.5 on 2019-09-20 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0022_remove_post_votes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comment_size',
            field=models.IntegerField(default=0),
        ),
    ]