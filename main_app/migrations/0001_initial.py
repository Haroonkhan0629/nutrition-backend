# Generated by Django 4.2.9 on 2024-03-02 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('muscle', models.CharField(verbose_name=20)),
                ('difficulty', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=300)),
                ('image', models.CharField(max_length=300)),
                ('saved', models.BooleanField(default=False)),
            ],
        ),
    ]