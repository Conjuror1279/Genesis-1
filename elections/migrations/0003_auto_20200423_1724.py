# Generated by Django 3.0.4 on 2020-04-23 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_elections'),
        ('elections', '0002_participant_votes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='society',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Elections'),
        ),
    ]
