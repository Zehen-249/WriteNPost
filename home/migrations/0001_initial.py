# Generated by Django 5.0.2 on 2024-04-28 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postName', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('author', models.TextField(max_length=100)),
            ],
        ),
    ]
