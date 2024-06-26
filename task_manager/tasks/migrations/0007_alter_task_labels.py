# Generated by Django 5.0.6 on 2024-06-13 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
        ('tasks', '0006_taskswithlabels_task_labels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='labels',
            field=models.ManyToManyField(related_name='labels', through='tasks.TasksWithLabels', to='labels.label'),
        ),
    ]
