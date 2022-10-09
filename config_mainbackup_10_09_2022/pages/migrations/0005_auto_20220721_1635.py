# Generated by Django 3.2.12 on 2022-07-21 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20220721_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backup_frontend',
            name='carloc',
            field=models.CharField(db_column='carOrLoc', max_length=255),
        ),
        migrations.AlterField(
            model_name='backup_frontend',
            name='l1n',
            field=models.DecimalField(db_column='L1N_pks', decimal_places=2, max_digits=25),
        ),
        migrations.AlterField(
            model_name='backup_frontend',
            name='l1s',
            field=models.DecimalField(db_column='L1S_pks', decimal_places=2, max_digits=25),
        ),
        migrations.AlterField(
            model_name='backup_frontend',
            name='v1n',
            field=models.DecimalField(db_column='V1N_pks', decimal_places=2, max_digits=25),
        ),
        migrations.AlterField(
            model_name='backup_frontend',
            name='v1s',
            field=models.DecimalField(db_column='V1S_pks', decimal_places=2, max_digits=25),
        ),
        migrations.AlterField(
            model_name='backup_frontend',
            name='v3n',
            field=models.DecimalField(db_column='V3N_pks', decimal_places=2, max_digits=25),
        ),
        migrations.AlterField(
            model_name='backup_frontend',
            name='v3n_prot',
            field=models.DecimalField(db_column='V3N Prot', decimal_places=2, max_digits=25),
        ),
        migrations.AlterField(
            model_name='backup_frontend',
            name='v3s',
            field=models.DecimalField(db_column='V3S_pks', decimal_places=2, max_digits=25),
        ),
    ]