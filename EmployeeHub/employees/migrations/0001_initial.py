# Generated by Django 4.2.4 on 2023-10-01 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('Phone', models.IntegerField(null=True)),
                ('Joined', models.DateField(null=True)),
                ('Departement', models.CharField(max_length=200)),
            ],
        ),
    ]