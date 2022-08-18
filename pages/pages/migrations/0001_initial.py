# Generated by Django 3.2.12 on 2022-04-21 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Metratr116',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
		('tr_id', models.IntegerField()),
                ('v1n', models.CharField(db_column='V1N', max_length=255)),
                ('v1s', models.CharField(db_column='V1S', max_length=255)),
                ('l1n', models.CharField(db_column='L1N', max_length=255)),
                ('l1s', models.CharField(db_column='L1S', max_length=255)),
                ('v3n', models.CharField(db_column='V3N', max_length=255)),
                ('v3s', models.CharField(db_column='V3S', max_length=255)),
                ('v3n_prot', models.CharField(db_column='V3N Prot', max_length=255)),
                ('trigger', models.CharField(db_column='Trigger', max_length=255)),
                ('speed', models.CharField(blank=True, db_column='Speed', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pages.djangocontenttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pages.authuser')),
            ],
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pages.authpermission')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pages.authuser')),
            ],
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pages.authgroup')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pages.authuser')),
            ],
        ),
        migrations.AddField(
            model_name='authpermission',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pages.djangocontenttype'),
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pages.authgroup')),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pages.authpermission')),
            ],
        ),
    ]