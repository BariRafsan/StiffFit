# Generated by Django 4.0 on 2022-01-04 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0003_auto_20220104_1216'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainerNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notif_msg', models.TextField()),
            ],
        ),
    ]
