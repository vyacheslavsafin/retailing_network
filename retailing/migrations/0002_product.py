# Generated by Django 5.0.1 on 2024-01-29 08:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retailing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='название')),
                ('model', models.CharField(max_length=100, verbose_name='модель')),
                ('release_date', models.DateField(verbose_name='дата выхода продукта на рынок')),
                ('dealer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retailing.dealer', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
