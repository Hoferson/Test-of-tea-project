# Generated by Django 4.2 on 2023-04-17 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0003_alter_achievements_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievements',
            name='position',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
