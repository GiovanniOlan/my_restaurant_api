# Generated by Django 4.0.5 on 2022-06-03 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalusercustom',
            old_name='usu_gender',
            new_name='usu_fkgender',
        ),
        migrations.RenameField(
            model_name='usercustom',
            old_name='usu_gender',
            new_name='usu_fkgender',
        ),
        migrations.AlterField(
            model_name='categorygender',
            name='catgen_description',
            field=models.CharField(max_length=50, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='historicalcategorygender',
            name='catgen_description',
            field=models.CharField(max_length=50, verbose_name='Descripción'),
        ),
    ]