# Generated by Django 2.1.5 on 2020-03-20 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='mascota',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Mascota',
        ),
    ]
