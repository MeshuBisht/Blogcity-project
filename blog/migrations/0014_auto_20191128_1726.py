# Generated by Django 2.2.7 on 2019-11-28 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20191030_0735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imgfile',
            field=models.ImageField(blank=True, default='', null=True, upload_to='images/'),
        ),
    ]
