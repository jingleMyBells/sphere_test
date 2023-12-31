# Generated by Django 4.2.7 on 2023-11-16 15:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='uuid')),
                ('brand', models.CharField(max_length=100, verbose_name='марка авто')),
                ('model', models.CharField(max_length=100, verbose_name='модель авто')),
                ('plate_number', models.CharField(max_length=10, verbose_name='номер авто')),
                ('owners_name', models.CharField(max_length=100, verbose_name='ФИО владельца')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='дата изменения')),
            ],
            options={
                'verbose_name': 'автомобиль',
                'verbose_name_plural': 'автомобили',
            },
        ),
    ]
