# Generated by Django 4.1.5 on 2023-01-27 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_alter_jobs_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='categoria',
            field=models.CharField(choices=[('D', 'Design'), ('EV', 'Edição de Vídeo'), ('T', 'Todos')], default='D', max_length=2),
        ),
    ]
