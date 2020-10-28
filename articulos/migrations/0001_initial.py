# Generated by Django 3.1.1 on 2020-10-27 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_Articulo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(help_text='Añada descripción del tipo artículo', max_length=50)),
            ],
            options={
                'ordering': ['descripcion'],
            },
        ),
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.IntegerField()),
                ('img', models.ImageField(blank=True, null=True, upload_to='img/')),
                ('stock', models.IntegerField()),
                ('tipoArticulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articulos.tipo_articulo')),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
    ]