# Generated by Django 4.0.4 on 2022-05-06 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_article_id_comment_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='level',
            field=models.IntegerField(default=1, verbose_name='comment level'),
        ),
    ]
