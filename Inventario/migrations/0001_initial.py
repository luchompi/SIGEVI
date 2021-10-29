# Generated by Django 3.2.8 on 2021-10-28 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Personas', '0001_initial'),
        ('Gestion', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Ingrese nombre del producto')),
                ('cantidad', models.IntegerField(verbose_name='Indique Cantidad de Producto')),
                ('uniades', models.CharField(choices=[('Unidad', 'Unidad'), ('Docena', 'Docena'), ('Resma', 'Resma'), ('Caja', 'Caja')], default='Unidad', max_length=12)),
                ('precio_compra', models.IntegerField(verbose_name='Indique el Valor del producto')),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Gestion.categoria', verbose_name='Seleccione Categoría del producto')),
                ('marca', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Gestion.marca', verbose_name='Especifique la marca del producto')),
                ('proveedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Personas.proveedor', verbose_name='Indique Proveedor')),
            ],
        ),
    ]
