# Generated by Django 4.0.1 on 2022-07-01 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_tickets_ticket'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, null=True)),
                ('description', models.CharField(max_length=500, null=True)),
                ('status', models.CharField(choices=[('New Project', 'New Project'), ('In Progress', 'In Progress'), ('Finished', 'Finished')], max_length=500, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]