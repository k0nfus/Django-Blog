# Generated by Django 4.1.6 on 2023-02-19 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_alter_comment_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=40),
        ),
    ]
