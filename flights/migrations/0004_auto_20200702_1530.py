# Generated by Django 3.0.7 on 2020-07-02 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_passenger'),
    ]

    operations = [
        migrations.RenameField(
            model_name='passenger',
            old_name='flight',
            new_name='flights',
        ),
    ]
