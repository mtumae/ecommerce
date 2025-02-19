# Generated by Django 5.1.6 on 2025-02-18 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('stock', models.IntegerField(blank=True, default=0, null=True)),
                ('price', models.IntegerField(blank=True, default=0, null=True)),
                ('item_type', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(upload_to='media/')),
            ],
        ),
    ]
