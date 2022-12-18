# Generated by Django 3.2 on 2022-12-17 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deliverables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'db_table': 'services_deliverables',
            },
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('precio', models.IntegerField()),
                ('deliverables', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deliverables', to='services.deliverables')),
            ],
            options={
                'db_table': 'services_package',
            },
        ),
        migrations.CreateModel(
            name='TypeServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='package', to='services.package')),
            ],
            options={
                'db_table': 'services_typeservices',
            },
        ),
    ]
