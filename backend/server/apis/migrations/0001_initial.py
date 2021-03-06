# Generated by Django 3.2.6 on 2021-12-02 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('cname', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('population', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'country',
            },
        ),
        migrations.CreateModel(
            name='Diseasetype',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, max_length=140, null=True)),
            ],
            options={
                'db_table': 'diseasetype',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('email', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('surname', models.CharField(blank=True, max_length=40, null=True)),
                ('salary', models.IntegerField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('cname', models.ForeignKey(blank=True, db_column='cname', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='apis.country')),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('email', models.OneToOneField(db_column='email', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='apis.users')),
                ('degree', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'doctor',
            },
        ),
        migrations.CreateModel(
            name='Publicservant',
            fields=[
                ('email', models.OneToOneField(db_column='email', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='apis.users')),
                ('department', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'publicservant',
            },
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('disease_code', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('pathogen', models.CharField(blank=True, max_length=20, null=True)),
                ('description', models.CharField(blank=True, max_length=140, null=True)),
                ('id', models.ForeignKey(blank=True, db_column='id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='apis.diseasetype')),
            ],
            options={
                'db_table': 'disease',
            },
        ),
        migrations.CreateModel(
            name='Specialize',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='apis.diseasetype')),
                ('email', models.ForeignKey(db_column='email', on_delete=django.db.models.deletion.DO_NOTHING, to='apis.doctor')),
            ],
            options={
                'db_table': 'specialize',
                'unique_together': {('id', 'email')},
            },
        ),
        migrations.CreateModel(
            name='Discover',
            fields=[
                ('cname', models.OneToOneField(db_column='cname', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='apis.country')),
                ('first_enc_date', models.DateField(blank=True, null=True)),
                ('disease_code', models.ForeignKey(db_column='disease_code', on_delete=django.db.models.deletion.DO_NOTHING, to='apis.disease')),
            ],
            options={
                'db_table': 'discover',
                'unique_together': {('cname', 'disease_code')},
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('email', models.OneToOneField(db_column='email', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='apis.publicservant')),
                ('total_deaths', models.IntegerField(blank=True, null=True)),
                ('total_patients', models.IntegerField(blank=True, null=True)),
                ('cname', models.ForeignKey(db_column='cname', on_delete=django.db.models.deletion.DO_NOTHING, to='apis.country')),
                ('disease_code', models.ForeignKey(db_column='disease_code', on_delete=django.db.models.deletion.DO_NOTHING, to='apis.disease')),
            ],
            options={
                'db_table': 'record',
                'unique_together': {('email', 'cname', 'disease_code')},
            },
        ),
    ]
