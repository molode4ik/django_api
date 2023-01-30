# Generated by Django 4.1.5 on 2023-01-30 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teaser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=300)),
                ('category', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=64)),
                ('status', models.CharField(blank=True, choices=[('paid', 'Оплачено'), ('failure', 'Отказ')], max_length=50)),
            ],
        ),
    ]