# Generated by Django 5.1.7 on 2025-03-18 13:21

import django.db.models.deletion
import django_fsm
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('state', django_fsm.FSMField(default='Pending', max_length=50)),
                ('order', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Workflow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('state', django_fsm.FSMField(default='Pending', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_state', models.CharField(max_length=50)),
                ('target_state', models.CharField(max_length=50)),
                ('source_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outgoing_links', to='workflow.task')),
                ('target_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incoming_links', to='workflow.task')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='workflow',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workflow', to='workflow.workflow'),
        ),
    ]
