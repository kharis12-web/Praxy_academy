# Generated by Django 2.2 on 2020-10-14 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.AlterField(
            model_name='prod',
            name='image',
            field=models.TextField(default=''),
        ),
    ]
