# Generated by Django 2.2.6 on 2019-10-25 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191025_0604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='color',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Technology', 'Technology'), ('Lifestyle', 'Lifestyle'), ('Nature', 'Nature'), ('Food', 'Food'), ('Tavel', 'Travel')], default='green', max_length=6),
        ),
    ]
