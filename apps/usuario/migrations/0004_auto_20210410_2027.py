# Generated by Django 3.1.7 on 2021-04-10 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_auto_20210410_2005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='id',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(default='no@mail', max_length=30, primary_key=True, serialize=False),
        ),
    ]
