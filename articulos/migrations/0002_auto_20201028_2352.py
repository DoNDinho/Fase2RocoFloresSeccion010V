# Generated by Django 3.1.1 on 2020-10-29 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='static/articulos/img/articulos'),
        ),
    ]
