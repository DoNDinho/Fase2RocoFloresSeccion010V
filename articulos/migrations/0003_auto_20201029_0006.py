# Generated by Django 3.1.1 on 2020-10-29 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0002_auto_20201028_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='articulos/static/articulos/img/articulos'),
        ),
    ]