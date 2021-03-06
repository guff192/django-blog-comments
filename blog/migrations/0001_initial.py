# Generated by Django 4.0.4 on 2022-05-05 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='article title')),
                ('text', models.TextField(max_length=5000, verbose_name='article text')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_posted', models.DateTimeField(auto_created=True, db_index=True, verbose_name='comment posting time')),
                ('level', models.IntegerField(verbose_name='comment level')),
                ('parent_path', models.CharField(db_index=True, max_length=255)),
                ('text', models.TextField(max_length=1000, verbose_name='comment text')),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.article')),
            ],
        ),
    ]
