# Generated by Django 4.1.2 on 2022-10-19 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_sociallink_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='iframe',
        ),
        migrations.AddField(
            model_name='productcolor',
            name='color',
            field=models.CharField(max_length=100, null=True),
        ),
    ]