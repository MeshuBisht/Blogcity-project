# Generated by Django 2.2.6 on 2019-10-30 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20191030_0535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('technology', 'Technology'), ('sports', 'Sports'), ('nature', 'Nature'), ('political', 'Political'), ('travel', 'Travel')], max_length=12),
        ),
    ]
