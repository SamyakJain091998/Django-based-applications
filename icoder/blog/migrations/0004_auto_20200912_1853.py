# Generated by Django 3.1.1 on 2020-09-12 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=25),
        ),
    ]
