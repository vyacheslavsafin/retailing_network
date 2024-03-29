# Generated by Django 5.0.1 on 2024-01-29 11:46

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retailing', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='dealer',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Время создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dealer',
            name='debt',
            field=models.IntegerField(default=0, verbose_name='Долг поставщику'),
        ),
        migrations.AddField(
            model_name='dealer',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='retailing.dealer', verbose_name='Поставщик'),
        ),
    ]
