# Generated by Django 2.2 on 2021-03-15 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='type_task',
        ),
        migrations.AddField(
            model_name='task',
            name='type_task',
            field=models.ManyToManyField(blank=True, related_name='type', to='webapp.Task_type'),
        ),
    ]
